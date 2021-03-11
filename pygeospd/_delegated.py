#
# Delegated Accessor Attributes
#
from functools import reduce
from collections.abc import Iterable
from warnings import warn
import numpy as np
import pandas as pd
import pygeos
from ._array import GeosArray

__all__ = [
    'get_SeriesProperty',
    'get_IndexedSeriesProperty',
    'get_IndexedDataFrameProperty',
    'get_ReturnMethodUnary',
    'get_SeriesMethodUnary',
    'get_IndexedSeriesMethodUnary',
    'get_IndexedDataFrameMethodUnary',
    'get_MethodBinary',
    'get_DataFrameExpandedProperty',
    'get_DataFrameExpandedMethodUnary',
]


def rgetattr(obj, attr, *args):
    def _getattr(obj, attr):
        return getattr(obj, attr, *args)
    return reduce(_getattr, [obj] + attr.split('.'))


def get_SeriesProperty(name, index=None, geos=False):
    """
    Create a property that returns a Series with values.
    This function is usually used for methods that have a many-to-1 relation with the original data.

    Args:
        name (str): Name of the method within the ``pygeos`` module.
        index (list): Values to use as the index of the returned Series; Default **None**.
        geos (bool, optional): Whether the returned data is PyGEOS dtype; Default **False**.
    """
    func = rgetattr(pygeos, name, None)
    func_summary = func.__doc__.strip().splitlines()[0]
    if func is None:
        raise AttributeError(f'Could not find function "pygeos.{name}"')

    def delegated(self):
        """
        {summary}

        Applies :func:`pygeos.{func}` to the data and returns a Series with the result.

        Returns:
            pd.Series: Series with the results of the function.
        """
        result = func(self._obj.array.data)
        if geos:
            result = GeosArray(result)

        return pd.Series(result, index=index, name=func.__name__)

    delegated.__doc__ = delegated.__doc__.format(func=name, summary=func_summary)
    if index is not None:
        delegated.__DataFrameExpand__ = 2
    return property(delegated)


def get_IndexedSeriesProperty(name, geos=False):
    """
    Create a property that returns a Series with values and the same index as the original data.
    This function is used for methods that have a 1-to-1 relation with the original data.

    Args:
        name (str): Name of the method within the ``pygeos`` module.
        geos (bool, optional): Whether the returned data is PyGEOS dtype; Default **False**.
    """
    func = rgetattr(pygeos, name, None)
    func_summary = func.__doc__.strip().splitlines()[0]
    if func is None:
        raise AttributeError(f'Could not find function "pygeos.{name}"')

    def delegated(self):
        """
        {summary}

        Applies :func:`pygeos.{func}` to the data and returns a Series with the result.

        Returns:
            pd.Series: Series with the result of the function and the same index.
        """
        result = func(self._obj.array.data)
        if geos:
            result = GeosArray(result)

        return pd.Series(result, index=self._obj.index, name=func.__name__)

    delegated.__doc__ = delegated.__doc__.format(func=name, summary=func_summary)
    delegated.__DataFrameExpand__ = 1
    return property(delegated)


def get_IndexedDataFrameProperty(name, columns, geos=False):
    """
    Create a property that returns a DataFrame with values and the same index as the original data.
    This function is used for methods that have a 1-to-many relation with the original data.

    Args:
        name (str): Name of the method within the ``pygeos`` module.
        columns (list<str>): List with column names.
        geos (bool or list<bool>, optional): Whether the returned data is PyGEOS dtype; Default **False**.

    Note:
        If the returned data has different dtypes, you can pass a list of booleans for the ``geos`` argument.
    """
    func = rgetattr(pygeos, name, None)
    func_summary = func.__doc__.strip().splitlines()[0]
    if func is None:
        raise AttributeError(f'Could not find function "pygeos.{name}"')

    if isinstance(geos, bool):
        geos = [geos] * len(columns)

    def delegated(self):
        """
        {summary}

        Applies :func:`pygeos.{func}` to the data and returns a DataFrame with the result.

        Returns:
            pd.DataFrame: Dataframe with the results of the function and the same index.
        """
        result = func(self._obj.array.data)
        if any(geos):
            result = [GeosArray(result[:, i]) if g else result[:, i] for g,i in zip(geos, range(result.shape[1]))]

        return pd.DataFrame(result, index=self._obj.index, columns=columns)

    return property(delegated, doc=delegated.__doc__.format(func=name, summary=func_summary))


def get_ReturnMethodUnary(name):
    """
    Create a unary method that returns the output of the function unmodified.

    Args:
        name (str): Name of the method within the ``pygeos`` module.
    """
    func = rgetattr(pygeos, name, None)
    func_summary = func.__doc__.strip().splitlines()[0]
    if func is None:
        raise AttributeError(f'Could not find function "pygeos.{name}"')

    def delegated(self, *args, **kwargs):
        """
        {summary}

        Applies :func:`pygeos.{func}` to the data and returns result unmodified.

        Args:
            args: Arguments passed to :func:`pygeos.{func}` after the first argument.
            kwargs: Keyword arguments passed to :func:`pygeos.{func}`.
        """
        return func(self._obj.array.data, *args, **kwargs)

    delegated.__doc__ = delegated.__doc__.format(func=name, summary=func_summary)
    return delegated


def get_SeriesMethodUnary(name, index=None, geos=False):
    """
    Create a unary method that returns a Series with values.
    This function is usually used for methods that have a many-to-1 relation with the original data.

    Args:
        name (str): Name of the method within the ``pygeos`` module.
        index (list): Values to use as the index of the returned Series; Default **None**.
        geos (bool, optional): Whether the returned data is PyGEOS dtype; Default **False**.
    """
    func = rgetattr(pygeos, name, None)
    func_summary = func.__doc__.strip().splitlines()[0]
    if func is None:
        raise AttributeError(f'Could not find function "pygeos.{name}"')

    def delegated(self, *args, **kwargs):
        """
        {summary}

        Applies :func:`pygeos.{func}` to the data and returns a Series with the result.

        Args:
            args: Arguments passed to :func:`pygeos.{func}` after the first argument.
            kwargs: Keyword arguments passed to :func:`pygeos.{func}`.

        Returns:
            pd.Series: Series with the results of the function.
        """
        result = func(self._obj.array.data, *args, **kwargs)
        if geos:
            result = GeosArray(result)

        return pd.Series(result, index=index, name=func.__name__)

    delegated.__doc__ = delegated.__doc__.format(func=name, summary=func_summary)
    if index is not None:
        delegated.__DataFrameExpand__ = 2
    return delegated


def get_IndexedSeriesMethodUnary(name, geos=False):
    """
    Create a unary method that returns a Series with values and the same index as the original data.
    This function is used for methods that have a 1-to-1 relation with the original data.

    Args:
        name (str): Name of the method within the ``pygeos`` module.
        geos (bool, optional): Whether the returned data is PyGEOS dtype; Default **False**.
    """
    func = rgetattr(pygeos, name, None)
    func_summary = func.__doc__.strip().splitlines()[0]
    if func is None:
        raise AttributeError(f'Could not find function "pygeos.{name}"')

    def delegated(self, *args, **kwargs):
        """
        {summary}

        Applies :func:`pygeos.{func}` to the data and returns a Series with the result.

        Args:
            args: Arguments passed to :func:`pygeos.{func}` after the first argument.
            kwargs: Keyword arguments passed to :func:`pygeos.{func}`.

        Returns:
            pd.Series: Series with the result of the function and the same index.
        """
        result = func(self._obj.array.data, *args, **kwargs)
        if geos:
            result = GeosArray(result)

        return pd.Series(result, index=self._obj.index, name=func.__name__)

    delegated.__doc__ = delegated.__doc__.format(func=name, summary=func_summary)
    delegated.__DataFrameExpand__ = 1
    return delegated


def get_IndexedDataFrameMethodUnary(name, columns, geos=False):
    """
    Create a unary method that returns a DataFrame with values and the same index as the original data.
    This function is used for methods that have a 1-to-many relation with the original data.

    Args:
        name (str): Name of the method within the ``pygeos`` module.
        columns (list<str>): List with column names.
        geos (bool or list<bool>, optional): Whether the returned data is PyGEOS dtype; Default **False**.

    Note:
        If the returned data has different dtypes, you can pass a list of booleans for the ``geos`` argument.
    """
    func = rgetattr(pygeos, name, None)
    func_summary = func.__doc__.strip().splitlines()[0]
    if func is None:
        raise AttributeError(f'Could not find function "pygeos.{name}"')

    if isinstance(geos, bool):
        geos = [geos] * len(columns)

    def delegated(self, *args, **kwargs):
        """
        {summary}

        Applies :func:`pygeos.{func}` to the data and returns a DataFrame with the result.

        Args:
            args: Arguments passed to :func:`pygeos.{func}` after the first argument.
            kwargs: Keyword arguments passed to :func:`pygeos.{func}`.

        Returns:
            pd.DataFrame: Dataframe with the results of the function and the same index.
        """
        result = func(self._obj.array.data, *args, **kwargs)
        if any(geos):
            result = [GeosArray(result[:, i]) if g else result[:, i] for g,i in zip(geos, range(result.shape[1]))]

        return pd.DataFrame(result, index=self._obj.index, columns=columns)

    delegated.__doc__ = delegated.__doc__.format(func=name, summary=func_summary)
    return delegated


def get_MethodBinary(name, geos=False):
    """
    Create a unary method that returns a DataFrame with values and the same index as the original data.
    This function is used for methods that have a 1-to-many relation with the original data.

    Args:
        name (str): Name of the method within the ``pygeos`` module.
        geos (bool, optional): Whether the returned data is PyGEOS dtype; Default **False**.
    """
    func = rgetattr(pygeos, name, None)
    func_summary = func.__doc__.strip().splitlines()[0]
    if func is None:
        raise AttributeError(f'Could not find function "pygeos.{name}"')

    def delegated(self, other=None, manner=None, **kwargs):
        """
        {summary}

        Applies :func:`pygeos.{func}` to ``(self, other)`` and returns the result.
        If no ``other`` data is given, the function gets applied to all possible combinations of the ``self`` data, by expanding the array.

        Args:
            other (pd.Series or np.ndarray or pygeos.Geometry, optional): Second argument to :func:`pygeos.{func}`; Default **self**
            manner ('keep' or 'align' or 'expand', optional): How to apply the :func:`pygeos.{func}` to the data; Default **None** 
            kwargs: Extra arguments, check :func:`pygeos.{func}` for more details.

        Returns:
            pd.Series: Series with the result of the function applied to self and other, with the same index as self.
            np.ndarray: 2-Dimensional array with the results of the function applied to each combination of geometries between self and other.

        Raises:
            ValueError: ``other`` argument is not a geos Series or PyGEOS NumPy Array

        Note:
            The ``manner`` argument dictates how the data gets transformed before applying :func:`pygeos.{func}`:
            
            - __'keep'__:
                Keep the original data as is and simply run the function.
                This returns a Series where the index is the same as the ``self`` data.
            - __'align'__:
                Align both Series according to their index, before running the function (we align the data according the ``self`` data).
                This returns a Series where the index is the same as the ``self`` data.
            - __'expand'__:
                Expand the data with a new index, before running the function.
                This means that the result will be an array of dimensions ``<len(a), len(b)>`` containing the result of all possible combinations of geometries.
                
            Of course, not every method is applicable for each type of ``other`` input.
            Here are the allowed manners for each type of input, as well as the default value:

            - __Series__: 'keep', 'align', 'expand' (default: 'align')
            - __1D ndarray__: 'keep', 'expand' (default: 'keep')
            - __nD ndarray__: 'keep' (default: 'keep')
            - __Geometry__: 'keep' (default: 'keep')
            - __None__ (aka. use self): 'expand' (default: 'expand')
        """
        if manner is not None:
            manner = manner[0].lower()

        if other is None:
            if manner is not None and manner != 'e':
                warn('When no other is given, we always "expand" to an array')
            data = self._obj.array.data[:, np.newaxis]
            other = self._obj.array.data[np.newaxis, :]
        elif isinstance(other, pd.Series):
            if not (pd.api.types.pandas_dtype('geos') == other.dtype):
                raise ValueError('"other" should be of dtype "geos".')
            
            if manner == 'e':
                data = self._obj.array.data[:, np.newaxis]
                other = other.array.data[np.newaxis, :]
            else:
                this = self._obj
                if (manner is None or manner == 'a') and not this.index.equals(other.index):
                    warn("The indices of the two Series are different, so we align them.")
                    this, other = this.align(other)

                data = this.array.data
                other = other.array.data
        elif isinstance(other, np.ndarray):
            if other.ndim == 1:
                data = self._obj.array.data
                if manner == 'e':
                    data = self._obj.array.data[:, np.newaxis]
                    other = other[np.newaxis, :]
                elif manner == 'a':
                    warn('Cannot align a NumPy Array.')
            else:
                if manner == 'e':
                    warn('Cannot expand a multi-dimensional NumPy Array')
                elif manner == 'a':
                    warn('Cannot align a NumPy Array.')

                data = self._obj.array.data
        elif isinstance(other, pygeos.lib.Geometry):
            data = self._obj.array.data
            if manner is not None and manner != 'k':
                warn('Cannot align or expand a single Geometry')
        else:
            raise ValueError('"other" should be a geos Series or PyGEOS NumPy array')

        result = func(data, other, **kwargs)
        if not isinstance(result, np.ndarray):
            result = result if isinstance(result, Iterable) else [result]
            result = np.array(result)

        if result.ndim == 1 and result.shape[0] == self._obj.shape[0]:
            if geos:
                result = GeosArray(result)
            return pd.Series(result, index=self._obj.index, name=func.__name__)
        else:
            return result

    delegated.__doc__ = delegated.__doc__.format(func=name, summary=func_summary)
    return delegated


def get_DataFrameExpandedProperty(name, expansion):
    """
    Create a property that calls the :class:`pygeospd.GeosSeriesAccessor` property
    on each geos column and groups the result.

    Args:
        name (str): Name of the propery in the :class:`pygeospd.GeosSeriesAccessor`.
        expansion (int): Type of dataframe expansion
    """
    func_summary = getattr(pygeos, name).__doc__.strip().splitlines()[0]

    def delegated1(self, inplace=False):
        """ 
        {summary}

        Applies :attr:`pygeospd.GeosSeriesAccessor.{func}` to each column of "geos" dtype
        and aggregates the results in a DataFrame.
        This means that for each geos column, we call :func:`pygeos.{func}`.

        Args:
            inplace (bool, optional): Whether to perform the modifications inplace; Default **False**.

        Returns:
            pd.DataFrame or None:
                DataFrame where each "geos" column from the original is transformed or None if ``inplace=True``.
        """
        result = {}
        for column, dtype in self._obj.dtypes.iteritems():
            if pd.api.types.pandas_dtype('geos') == dtype:
                result[column] = getattr(self._obj[column].geos, name)

        if not inplace:
            return pd.DataFrame.from_dict(result)
        else:
            for column, values in result.items():
                self._obj[column] = values

    def delegated2(self):
        """ 
        {summary}

        Applies :attr:`pygeospd.GeosSeriesAccessor.{func}` to each column of "geos" dtype
        and aggregates the results in a DataFrame.
        This means that for each geos column, we call :func:`pygeos.{func}`.

        Returns:
            pd.DataFrame: DataFrame where each "geos" column from the original is transformed.
        """
        result = {}
        for column, dtype in self._obj.dtypes.iteritems():
            if pd.api.types.pandas_dtype('geos') == dtype:
                result[column] = getattr(self._obj[column].geos, name)

        return pd.DataFrame.from_dict(result)

    if expansion == 1:
        delegated1.__doc__ = delegated1.__doc__.format(func=name, summary=func_summary)
        return delegated1
    else:
        delegated2.__doc__ = delegated2.__doc__.format(func=name, summary=func_summary)
        return property(delegated2)


def get_DataFrameExpandedMethodUnary(name, expansion):
    """
    Create a unary method that calls the :class:`pygeospd.GeosSeriesAccessor` method
    on each geos column and aggregates the result.

    Args:
        name (str): Name of the method in the :class:`pygeospd.GeosSeriesAccessor`.
        expansion (int): Type of dataframe expansion
    """
    func_summary = getattr(pygeos, name).__doc__.strip().splitlines()[0]

    def delegated1(self, *args, inplace=False, **kwargs):
        """ 
        {summary}

        Applies :func:`pygeospd.GeosSeriesAccessor.{func}` to each column of "geos" dtype
        and aggregates the results in a DataFrame.
        This means that for each geos column, we call :func:`pygeos.{func}`.

        Args:
            args: Arguments passed to :func:`pygeos.{func}` after the first argument.
            inplace (bool, optional): Whether to perform the modifications inplace; Default **False**.
            kwargs: Keyword arguments passed to :func:`pygeos.{func}`.

        Returns:
            pd.DataFrame or None:
                DataFrame where each "geos" column from the original is transformed or None if ``inplace=True``.
        """
        result = {}
        for column, dtype in self._obj.dtypes.iteritems():
            if pd.api.types.pandas_dtype('geos') == dtype:
                result[column] = getattr(self._obj[column].geos, name)(*args, **kwargs)

        if not inplace:
            return pd.DataFrame.from_dict(result)
        else:
            for column, values in result.items():
                self._obj[column] = values

    def delegated2(self, *args, **kwargs):
        """ 
        {summary}

        Applies :func:`pygeospd.GeosSeriesAccessor.{func}` to each column of "geos" dtype
        and aggregates the results in a DataFrame.
        This means that for each geos column, we call :func:`pygeos.{func}`.

        Args:
            args: Arguments passed to :func:`pygeos.{func}` after the first argument.
            kwargs: Keyword arguments passed to :func:`pygeos.{func}`.

        Returns:
            pd.DataFrame or None:
                DataFrame where each "geos" column from the original is transformed or None if ``inplace=True``.
        """
        result = {}
        for column, dtype in self._obj.dtypes.iteritems():
            if pd.api.types.pandas_dtype('geos') == dtype:
                result[column] = getattr(self._obj[column].geos, name)(*args, **kwargs)

        return pd.DataFrame.from_dict(result)

    if expansion == 1:
        delegated1.__doc__ = delegated1.__doc__.format(func=name, summary=func_summary)
        return delegated1
    else:
        delegated2.__doc__ = delegated2.__doc__.format(func=name, summary=func_summary)
        return delegated2
