# encoding: utf-8
# module statsmodels.tsa.innovations._arma_innovations
# from C:\Users\Doly\Anaconda3\lib\site-packages\statsmodels\tsa\innovations\_arma_innovations.cp37-win_amd64.pyd
# by generator 1.147
"""
Innovations algorithm

Author: Chad Fulton
License: Simplified-BSD
"""

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import numpy as np # C:\Users\Doly\Anaconda3\lib\site-packages\numpy\__init__.py
import warnings as warnings # C:\Users\Doly\Anaconda3\lib\warnings.py
import statsmodels.tsa.arima_process as arima_process # C:\Users\Doly\Anaconda3\lib\site-packages\statsmodels\tsa\arima_process.py

# functions

def carma_innovations(*args, **kwargs): # real signature unknown
    """
    arma_innovations(cnp.complex64_t [:] endog, cnp.complex64_t [:] ar_params, cnp.complex64_t [:] ma_params):
        
        Compute innovations and variances based on an ARMA process.
    
        Parameters
        ----------
        endog : ndarray
            The observed time-series process.
        ar_params : ndarray
            Autoregressive parameters.
        ma_params : ndarray
            Moving average parameters.
        sigma2 : ndarray
            The ARMA innovation variance.
    
        Returns
        -------
        u : ndarray
            The vector of innovations: the one-step-ahead prediction errors from
            applying the innovations algorithm.
        v : ndarray
            The vector of innovation variances.
    
        Notes
        -----
        The innovations algorithm is presented in _[1], section 2.5.2.
    
        References
        ----------
        .. [1] Brockwell, Peter J., and Richard A. Davis. 2009.
           Time Series: Theory and Methods. 2nd ed. 1991.
           New York, NY: Springer.
    """
    pass

def carma_innovations_algo_fast(*args, **kwargs): # real signature unknown
    """
    arma_innovations_algo_fast(int nobs, cnp.complex64_t [:] ar_params, cnp.complex64_t [:] ma_params, cnp.complex64_t [:, :] acovf, cnp.complex64_t [:] acovf2)
        
        Quickly apply innovations algorithm for an ARMA process.
    
        Parameters
        ----------
        ar_params : ndarray
            Autoregressive parameters.
        ma_params : ndarray
            Moving average parameters.
        acovf : ndarray
            An `m * 2` x `m * 2` autocovariance matrix at least the first `m`
            columns filled in, where `m = max(len(ar_params), ma_params)`
            (see `arma_transformed_acovf_fast`).
        acovf2 : ndarray
            A `max(0, nobs - m)` length vector containing the autocovariance
            function associated with the final `nobs - m` observations.
    
        Returns
        -------
        theta : ndarray
            The matrix of moving average coefficients from the innovations
            algorithm.
        v : ndarray
            The vector of mean squared errors.
    
        Notes
        -----
        The innovations algorithm is presented in _[1], section 2.5.2.
    
        Details of the innovations algorithm applied to ARMA processes is given
        in _[1] section 3.3 and in section 5.2.7.
    
        This function is relatively fast even with a large number of observations
        since we can exploit a number of known zeros in the theta array.
    
        References
        ----------
        .. [1] Brockwell, Peter J., and Richard A. Davis. 2009.
           Time Series: Theory and Methods. 2nd ed. 1991.
           New York, NY: Springer.
    """
    pass

def carma_innovations_filter(*args, **kwargs): # real signature unknown
    """
    arma_innovations_filter(cnp.complex64_t [:] endog, cnp.complex64_t [:] ar_params, cnp.complex64_t [:] ma_params, cnp.complex64_t [:, :] theta):
        
        Innovations filter for an ARMA process.
    
        Parameters
        ----------
        endog : ndarray
            The observed time-series process.
        ar_params : ndarray
            Autoregressive parameters.
        ma_params : ndarray
            Moving average parameters.
        theta : ndarray
            The matrix of moving average coefficients from the innovations
            algorithm (see `arma_innovations_algo` or `arma_innovations_algo_fast`)
    
        Returns
        -------
        u : ndarray
            The vector of innovations: the one-step-ahead prediction errors from
            applying the innovations algorithm.
    
        Notes
        -----
        The innovations algorithm is presented in _[1], section 2.5.2.
    
        Details of the innovations algorithm applied to ARMA processes is given
        in _[1] section 3.3 and in section 5.2.7.
    
        References
        ----------
        .. [1] Brockwell, Peter J., and Richard A. Davis. 2009.
           Time Series: Theory and Methods. 2nd ed. 1991.
           New York, NY: Springer.
    """
    pass

def carma_loglikeobs_fast(cnp_complex64_t, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    carma_loglikeobs_fast(cnp.complex64_t [:] endog, cnp.complex64_t [:] ar_params, cnp.complex64_t [:] ma_params, cnp.complex64_t sigma2)
    
        Quickly calculate the loglikelihood of each observation for an ARMA process
    
        Parameters
        ----------
        endog : ndarray
            The observed time-series process.
        ar_params : ndarray
            Autoregressive parameters.
        ma_params : ndarray
            Moving average parameters.
        sigma2 : ndarray
            The ARMA innovation variance.
    
        Returns
        -------
        loglike : ndarray of float
            Array of loglikelihood values for each observation.
    
        Notes
        -----
        Details related to computing the loglikelihood associated with an ARMA
        process using the innovations algorithm are given in _[1] section 5.2.
    
        References
        ----------
        .. [1] Brockwell, Peter J., and Richard A. Davis. 2009.
           Time Series: Theory and Methods. 2nd ed. 1991.
           New York, NY: Springer.
    """
    pass

def carma_transformed_acovf_fast(*args, **kwargs): # real signature unknown
    """
    arma_transformed_acovf_fast(cnp.complex64_t [:] ar, cnp.complex64_t [:] ma, cnp.complex64_t [:] arma_acovf)
        
        Quickly construct the autocovariance matrix for a transformed process.
    
        Using the autocovariance function for an ARMA process, constructs the
        autocovariances associated with the transformed process described
        in equation (3.3.1) of _[1] in a memory efficient, and so fast, way.
    
        Parameters
        ----------
        ar : ndarray
            Autoregressive coefficients, including the zero lag, where the sign
            convention assumes the coefficients are part of the lag polynomial on
            the left-hand-side of the ARMA definition (i.e. they have the opposite
            sign from the usual econometrics convention in which the coefficients
            are on the right-hand-side of the ARMA definition).
        ma : ndarray
            Moving average coefficients, including the zero lag, where the sign
            convention assumes the coefficients are part of the lag polynomial on
            the right-hand-side of the ARMA definition (i.e. they have the same
            sign from the usual econometrics convention in which the coefficients
            are on the right-hand-side of the ARMA definition).
        arma_acovf : ndarray
            The vector of autocovariances of the ARMA process.
    
        Returns
        -------
        acovf : ndarray
            A matrix containing the autocovariances of the portion of the
            transformed process with time-varying autocovariances. Its dimension
            is equal to `min(m * 2, n)` where `m = max(len(ar) - 1, len(ma) - 1)`
            and `n` is the length of the input array `arma_acovf`. It is important
            to note that only the values in the first `m` columns or `m` rows are
            valid. In particular, the entries in the block `acovf[m:, m:]` should
            not be used in any case (and in fact will always be equal to zeros).
        acovf2 : ndarray
            An array containing the autocovariance function of the portion of the
            transformed process with time-invariant autocovariances. Its dimension
            is equal to `max(n - m, 0)` where `n` is the length of the input
            array `arma_acovf`.
    
        Notes
        -----
        The definition of this autocovariance matrix is from _[1] equation 3.3.3.
    
        This function assumes that the variance of the ARMA innovation term is
        equal to one. If this is not true, then the calling program should replace
        `arma_acovf` with `arma_acovf / sigma2`, where sigma2 is that variance.
    
        This function is relatively fast even when `arma_acovf` is large, since
        it only constructs the full autocovariance matrix for a generally small
        subset of observations. The trade-off is that the output of this function
        is somewhat more difficult to use.
    
        References
        ----------
        .. [1] Brockwell, Peter J., and Richard A. Davis. 2009.
           Time Series: Theory and Methods. 2nd ed. 1991.
           New York, NY: Springer.
    """
    pass

def darma_innovations(*args, **kwargs): # real signature unknown
    """
    arma_innovations(cnp.float64_t [:] endog, cnp.float64_t [:] ar_params, cnp.float64_t [:] ma_params):
        
        Compute innovations and variances based on an ARMA process.
    
        Parameters
        ----------
        endog : ndarray
            The observed time-series process.
        ar_params : ndarray
            Autoregressive parameters.
        ma_params : ndarray
            Moving average parameters.
        sigma2 : ndarray
            The ARMA innovation variance.
    
        Returns
        -------
        u : ndarray
            The vector of innovations: the one-step-ahead prediction errors from
            applying the innovations algorithm.
        v : ndarray
            The vector of innovation variances.
    
        Notes
        -----
        The innovations algorithm is presented in _[1], section 2.5.2.
    
        References
        ----------
        .. [1] Brockwell, Peter J., and Richard A. Davis. 2009.
           Time Series: Theory and Methods. 2nd ed. 1991.
           New York, NY: Springer.
    """
    pass

def darma_innovations_algo_fast(*args, **kwargs): # real signature unknown
    """
    arma_innovations_algo_fast(int nobs, cnp.float64_t [:] ar_params, cnp.float64_t [:] ma_params, cnp.float64_t [:, :] acovf, cnp.float64_t [:] acovf2)
        
        Quickly apply innovations algorithm for an ARMA process.
    
        Parameters
        ----------
        ar_params : ndarray
            Autoregressive parameters.
        ma_params : ndarray
            Moving average parameters.
        acovf : ndarray
            An `m * 2` x `m * 2` autocovariance matrix at least the first `m`
            columns filled in, where `m = max(len(ar_params), ma_params)`
            (see `arma_transformed_acovf_fast`).
        acovf2 : ndarray
            A `max(0, nobs - m)` length vector containing the autocovariance
            function associated with the final `nobs - m` observations.
    
        Returns
        -------
        theta : ndarray
            The matrix of moving average coefficients from the innovations
            algorithm.
        v : ndarray
            The vector of mean squared errors.
    
        Notes
        -----
        The innovations algorithm is presented in _[1], section 2.5.2.
    
        Details of the innovations algorithm applied to ARMA processes is given
        in _[1] section 3.3 and in section 5.2.7.
    
        This function is relatively fast even with a large number of observations
        since we can exploit a number of known zeros in the theta array.
    
        References
        ----------
        .. [1] Brockwell, Peter J., and Richard A. Davis. 2009.
           Time Series: Theory and Methods. 2nd ed. 1991.
           New York, NY: Springer.
    """
    pass

def darma_innovations_filter(*args, **kwargs): # real signature unknown
    """
    arma_innovations_filter(cnp.float64_t [:] endog, cnp.float64_t [:] ar_params, cnp.float64_t [:] ma_params, cnp.float64_t [:, :] theta):
        
        Innovations filter for an ARMA process.
    
        Parameters
        ----------
        endog : ndarray
            The observed time-series process.
        ar_params : ndarray
            Autoregressive parameters.
        ma_params : ndarray
            Moving average parameters.
        theta : ndarray
            The matrix of moving average coefficients from the innovations
            algorithm (see `arma_innovations_algo` or `arma_innovations_algo_fast`)
    
        Returns
        -------
        u : ndarray
            The vector of innovations: the one-step-ahead prediction errors from
            applying the innovations algorithm.
    
        Notes
        -----
        The innovations algorithm is presented in _[1], section 2.5.2.
    
        Details of the innovations algorithm applied to ARMA processes is given
        in _[1] section 3.3 and in section 5.2.7.
    
        References
        ----------
        .. [1] Brockwell, Peter J., and Richard A. Davis. 2009.
           Time Series: Theory and Methods. 2nd ed. 1991.
           New York, NY: Springer.
    """
    pass

def darma_loglikeobs_fast(cnp_float64_t, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    darma_loglikeobs_fast(cnp.float64_t [:] endog, cnp.float64_t [:] ar_params, cnp.float64_t [:] ma_params, cnp.float64_t sigma2)
    
        Quickly calculate the loglikelihood of each observation for an ARMA process
    
        Parameters
        ----------
        endog : ndarray
            The observed time-series process.
        ar_params : ndarray
            Autoregressive parameters.
        ma_params : ndarray
            Moving average parameters.
        sigma2 : ndarray
            The ARMA innovation variance.
    
        Returns
        -------
        loglike : ndarray of float
            Array of loglikelihood values for each observation.
    
        Notes
        -----
        Details related to computing the loglikelihood associated with an ARMA
        process using the innovations algorithm are given in _[1] section 5.2.
    
        References
        ----------
        .. [1] Brockwell, Peter J., and Richard A. Davis. 2009.
           Time Series: Theory and Methods. 2nd ed. 1991.
           New York, NY: Springer.
    """
    pass

def darma_transformed_acovf_fast(*args, **kwargs): # real signature unknown
    """
    arma_transformed_acovf_fast(cnp.float64_t [:] ar, cnp.float64_t [:] ma, cnp.float64_t [:] arma_acovf)
        
        Quickly construct the autocovariance matrix for a transformed process.
    
        Using the autocovariance function for an ARMA process, constructs the
        autocovariances associated with the transformed process described
        in equation (3.3.1) of _[1] in a memory efficient, and so fast, way.
    
        Parameters
        ----------
        ar : ndarray
            Autoregressive coefficients, including the zero lag, where the sign
            convention assumes the coefficients are part of the lag polynomial on
            the left-hand-side of the ARMA definition (i.e. they have the opposite
            sign from the usual econometrics convention in which the coefficients
            are on the right-hand-side of the ARMA definition).
        ma : ndarray
            Moving average coefficients, including the zero lag, where the sign
            convention assumes the coefficients are part of the lag polynomial on
            the right-hand-side of the ARMA definition (i.e. they have the same
            sign from the usual econometrics convention in which the coefficients
            are on the right-hand-side of the ARMA definition).
        arma_acovf : ndarray
            The vector of autocovariances of the ARMA process.
    
        Returns
        -------
        acovf : ndarray
            A matrix containing the autocovariances of the portion of the
            transformed process with time-varying autocovariances. Its dimension
            is equal to `min(m * 2, n)` where `m = max(len(ar) - 1, len(ma) - 1)`
            and `n` is the length of the input array `arma_acovf`. It is important
            to note that only the values in the first `m` columns or `m` rows are
            valid. In particular, the entries in the block `acovf[m:, m:]` should
            not be used in any case (and in fact will always be equal to zeros).
        acovf2 : ndarray
            An array containing the autocovariance function of the portion of the
            transformed process with time-invariant autocovariances. Its dimension
            is equal to `max(n - m, 0)` where `n` is the length of the input
            array `arma_acovf`.
    
        Notes
        -----
        The definition of this autocovariance matrix is from _[1] equation 3.3.3.
    
        This function assumes that the variance of the ARMA innovation term is
        equal to one. If this is not true, then the calling program should replace
        `arma_acovf` with `arma_acovf / sigma2`, where sigma2 is that variance.
    
        This function is relatively fast even when `arma_acovf` is large, since
        it only constructs the full autocovariance matrix for a generally small
        subset of observations. The trade-off is that the output of this function
        is somewhat more difficult to use.
    
        References
        ----------
        .. [1] Brockwell, Peter J., and Richard A. Davis. 2009.
           Time Series: Theory and Methods. 2nd ed. 1991.
           New York, NY: Springer.
    """
    pass

def sarma_innovations(*args, **kwargs): # real signature unknown
    """
    arma_innovations(cnp.float32_t [:] endog, cnp.float32_t [:] ar_params, cnp.float32_t [:] ma_params):
        
        Compute innovations and variances based on an ARMA process.
    
        Parameters
        ----------
        endog : ndarray
            The observed time-series process.
        ar_params : ndarray
            Autoregressive parameters.
        ma_params : ndarray
            Moving average parameters.
        sigma2 : ndarray
            The ARMA innovation variance.
    
        Returns
        -------
        u : ndarray
            The vector of innovations: the one-step-ahead prediction errors from
            applying the innovations algorithm.
        v : ndarray
            The vector of innovation variances.
    
        Notes
        -----
        The innovations algorithm is presented in _[1], section 2.5.2.
    
        References
        ----------
        .. [1] Brockwell, Peter J., and Richard A. Davis. 2009.
           Time Series: Theory and Methods. 2nd ed. 1991.
           New York, NY: Springer.
    """
    pass

def sarma_innovations_algo_fast(*args, **kwargs): # real signature unknown
    """
    arma_innovations_algo_fast(int nobs, cnp.float32_t [:] ar_params, cnp.float32_t [:] ma_params, cnp.float32_t [:, :] acovf, cnp.float32_t [:] acovf2)
        
        Quickly apply innovations algorithm for an ARMA process.
    
        Parameters
        ----------
        ar_params : ndarray
            Autoregressive parameters.
        ma_params : ndarray
            Moving average parameters.
        acovf : ndarray
            An `m * 2` x `m * 2` autocovariance matrix at least the first `m`
            columns filled in, where `m = max(len(ar_params), ma_params)`
            (see `arma_transformed_acovf_fast`).
        acovf2 : ndarray
            A `max(0, nobs - m)` length vector containing the autocovariance
            function associated with the final `nobs - m` observations.
    
        Returns
        -------
        theta : ndarray
            The matrix of moving average coefficients from the innovations
            algorithm.
        v : ndarray
            The vector of mean squared errors.
    
        Notes
        -----
        The innovations algorithm is presented in _[1], section 2.5.2.
    
        Details of the innovations algorithm applied to ARMA processes is given
        in _[1] section 3.3 and in section 5.2.7.
    
        This function is relatively fast even with a large number of observations
        since we can exploit a number of known zeros in the theta array.
    
        References
        ----------
        .. [1] Brockwell, Peter J., and Richard A. Davis. 2009.
           Time Series: Theory and Methods. 2nd ed. 1991.
           New York, NY: Springer.
    """
    pass

def sarma_innovations_filter(*args, **kwargs): # real signature unknown
    """
    arma_innovations_filter(cnp.float32_t [:] endog, cnp.float32_t [:] ar_params, cnp.float32_t [:] ma_params, cnp.float32_t [:, :] theta):
        
        Innovations filter for an ARMA process.
    
        Parameters
        ----------
        endog : ndarray
            The observed time-series process.
        ar_params : ndarray
            Autoregressive parameters.
        ma_params : ndarray
            Moving average parameters.
        theta : ndarray
            The matrix of moving average coefficients from the innovations
            algorithm (see `arma_innovations_algo` or `arma_innovations_algo_fast`)
    
        Returns
        -------
        u : ndarray
            The vector of innovations: the one-step-ahead prediction errors from
            applying the innovations algorithm.
    
        Notes
        -----
        The innovations algorithm is presented in _[1], section 2.5.2.
    
        Details of the innovations algorithm applied to ARMA processes is given
        in _[1] section 3.3 and in section 5.2.7.
    
        References
        ----------
        .. [1] Brockwell, Peter J., and Richard A. Davis. 2009.
           Time Series: Theory and Methods. 2nd ed. 1991.
           New York, NY: Springer.
    """
    pass

def sarma_loglikeobs_fast(cnp_float32_t, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    sarma_loglikeobs_fast(cnp.float32_t [:] endog, cnp.float32_t [:] ar_params, cnp.float32_t [:] ma_params, cnp.float32_t sigma2)
    
        Quickly calculate the loglikelihood of each observation for an ARMA process
    
        Parameters
        ----------
        endog : ndarray
            The observed time-series process.
        ar_params : ndarray
            Autoregressive parameters.
        ma_params : ndarray
            Moving average parameters.
        sigma2 : ndarray
            The ARMA innovation variance.
    
        Returns
        -------
        loglike : ndarray of float
            Array of loglikelihood values for each observation.
    
        Notes
        -----
        Details related to computing the loglikelihood associated with an ARMA
        process using the innovations algorithm are given in _[1] section 5.2.
    
        References
        ----------
        .. [1] Brockwell, Peter J., and Richard A. Davis. 2009.
           Time Series: Theory and Methods. 2nd ed. 1991.
           New York, NY: Springer.
    """
    pass

def sarma_transformed_acovf_fast(*args, **kwargs): # real signature unknown
    """
    arma_transformed_acovf_fast(cnp.float32_t [:] ar, cnp.float32_t [:] ma, cnp.float32_t [:] arma_acovf)
        
        Quickly construct the autocovariance matrix for a transformed process.
    
        Using the autocovariance function for an ARMA process, constructs the
        autocovariances associated with the transformed process described
        in equation (3.3.1) of _[1] in a memory efficient, and so fast, way.
    
        Parameters
        ----------
        ar : ndarray
            Autoregressive coefficients, including the zero lag, where the sign
            convention assumes the coefficients are part of the lag polynomial on
            the left-hand-side of the ARMA definition (i.e. they have the opposite
            sign from the usual econometrics convention in which the coefficients
            are on the right-hand-side of the ARMA definition).
        ma : ndarray
            Moving average coefficients, including the zero lag, where the sign
            convention assumes the coefficients are part of the lag polynomial on
            the right-hand-side of the ARMA definition (i.e. they have the same
            sign from the usual econometrics convention in which the coefficients
            are on the right-hand-side of the ARMA definition).
        arma_acovf : ndarray
            The vector of autocovariances of the ARMA process.
    
        Returns
        -------
        acovf : ndarray
            A matrix containing the autocovariances of the portion of the
            transformed process with time-varying autocovariances. Its dimension
            is equal to `min(m * 2, n)` where `m = max(len(ar) - 1, len(ma) - 1)`
            and `n` is the length of the input array `arma_acovf`. It is important
            to note that only the values in the first `m` columns or `m` rows are
            valid. In particular, the entries in the block `acovf[m:, m:]` should
            not be used in any case (and in fact will always be equal to zeros).
        acovf2 : ndarray
            An array containing the autocovariance function of the portion of the
            transformed process with time-invariant autocovariances. Its dimension
            is equal to `max(n - m, 0)` where `n` is the length of the input
            array `arma_acovf`.
    
        Notes
        -----
        The definition of this autocovariance matrix is from _[1] equation 3.3.3.
    
        This function assumes that the variance of the ARMA innovation term is
        equal to one. If this is not true, then the calling program should replace
        `arma_acovf` with `arma_acovf / sigma2`, where sigma2 is that variance.
    
        This function is relatively fast even when `arma_acovf` is large, since
        it only constructs the full autocovariance matrix for a generally small
        subset of observations. The trade-off is that the output of this function
        is somewhat more difficult to use.
    
        References
        ----------
        .. [1] Brockwell, Peter J., and Richard A. Davis. 2009.
           Time Series: Theory and Methods. 2nd ed. 1991.
           New York, NY: Springer.
    """
    pass

def zarma_innovations(*args, **kwargs): # real signature unknown
    """
    arma_innovations(cnp.complex128_t [:] endog, cnp.complex128_t [:] ar_params, cnp.complex128_t [:] ma_params):
        
        Compute innovations and variances based on an ARMA process.
    
        Parameters
        ----------
        endog : ndarray
            The observed time-series process.
        ar_params : ndarray
            Autoregressive parameters.
        ma_params : ndarray
            Moving average parameters.
        sigma2 : ndarray
            The ARMA innovation variance.
    
        Returns
        -------
        u : ndarray
            The vector of innovations: the one-step-ahead prediction errors from
            applying the innovations algorithm.
        v : ndarray
            The vector of innovation variances.
    
        Notes
        -----
        The innovations algorithm is presented in _[1], section 2.5.2.
    
        References
        ----------
        .. [1] Brockwell, Peter J., and Richard A. Davis. 2009.
           Time Series: Theory and Methods. 2nd ed. 1991.
           New York, NY: Springer.
    """
    pass

def zarma_innovations_algo_fast(*args, **kwargs): # real signature unknown
    """
    arma_innovations_algo_fast(int nobs, cnp.complex128_t [:] ar_params, cnp.complex128_t [:] ma_params, cnp.complex128_t [:, :] acovf, cnp.complex128_t [:] acovf2)
        
        Quickly apply innovations algorithm for an ARMA process.
    
        Parameters
        ----------
        ar_params : ndarray
            Autoregressive parameters.
        ma_params : ndarray
            Moving average parameters.
        acovf : ndarray
            An `m * 2` x `m * 2` autocovariance matrix at least the first `m`
            columns filled in, where `m = max(len(ar_params), ma_params)`
            (see `arma_transformed_acovf_fast`).
        acovf2 : ndarray
            A `max(0, nobs - m)` length vector containing the autocovariance
            function associated with the final `nobs - m` observations.
    
        Returns
        -------
        theta : ndarray
            The matrix of moving average coefficients from the innovations
            algorithm.
        v : ndarray
            The vector of mean squared errors.
    
        Notes
        -----
        The innovations algorithm is presented in _[1], section 2.5.2.
    
        Details of the innovations algorithm applied to ARMA processes is given
        in _[1] section 3.3 and in section 5.2.7.
    
        This function is relatively fast even with a large number of observations
        since we can exploit a number of known zeros in the theta array.
    
        References
        ----------
        .. [1] Brockwell, Peter J., and Richard A. Davis. 2009.
           Time Series: Theory and Methods. 2nd ed. 1991.
           New York, NY: Springer.
    """
    pass

def zarma_innovations_filter(*args, **kwargs): # real signature unknown
    """
    arma_innovations_filter(cnp.complex128_t [:] endog, cnp.complex128_t [:] ar_params, cnp.complex128_t [:] ma_params, cnp.complex128_t [:, :] theta):
        
        Innovations filter for an ARMA process.
    
        Parameters
        ----------
        endog : ndarray
            The observed time-series process.
        ar_params : ndarray
            Autoregressive parameters.
        ma_params : ndarray
            Moving average parameters.
        theta : ndarray
            The matrix of moving average coefficients from the innovations
            algorithm (see `arma_innovations_algo` or `arma_innovations_algo_fast`)
    
        Returns
        -------
        u : ndarray
            The vector of innovations: the one-step-ahead prediction errors from
            applying the innovations algorithm.
    
        Notes
        -----
        The innovations algorithm is presented in _[1], section 2.5.2.
    
        Details of the innovations algorithm applied to ARMA processes is given
        in _[1] section 3.3 and in section 5.2.7.
    
        References
        ----------
        .. [1] Brockwell, Peter J., and Richard A. Davis. 2009.
           Time Series: Theory and Methods. 2nd ed. 1991.
           New York, NY: Springer.
    """
    pass

def zarma_loglikeobs_fast(cnp_complex128_t, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    zarma_loglikeobs_fast(cnp.complex128_t [:] endog, cnp.complex128_t [:] ar_params, cnp.complex128_t [:] ma_params, cnp.complex128_t sigma2)
    
        Quickly calculate the loglikelihood of each observation for an ARMA process
    
        Parameters
        ----------
        endog : ndarray
            The observed time-series process.
        ar_params : ndarray
            Autoregressive parameters.
        ma_params : ndarray
            Moving average parameters.
        sigma2 : ndarray
            The ARMA innovation variance.
    
        Returns
        -------
        loglike : ndarray of float
            Array of loglikelihood values for each observation.
    
        Notes
        -----
        Details related to computing the loglikelihood associated with an ARMA
        process using the innovations algorithm are given in _[1] section 5.2.
    
        References
        ----------
        .. [1] Brockwell, Peter J., and Richard A. Davis. 2009.
           Time Series: Theory and Methods. 2nd ed. 1991.
           New York, NY: Springer.
    """
    pass

def zarma_transformed_acovf_fast(*args, **kwargs): # real signature unknown
    """
    arma_transformed_acovf_fast(cnp.complex128_t [:] ar, cnp.complex128_t [:] ma, cnp.complex128_t [:] arma_acovf)
        
        Quickly construct the autocovariance matrix for a transformed process.
    
        Using the autocovariance function for an ARMA process, constructs the
        autocovariances associated with the transformed process described
        in equation (3.3.1) of _[1] in a memory efficient, and so fast, way.
    
        Parameters
        ----------
        ar : ndarray
            Autoregressive coefficients, including the zero lag, where the sign
            convention assumes the coefficients are part of the lag polynomial on
            the left-hand-side of the ARMA definition (i.e. they have the opposite
            sign from the usual econometrics convention in which the coefficients
            are on the right-hand-side of the ARMA definition).
        ma : ndarray
            Moving average coefficients, including the zero lag, where the sign
            convention assumes the coefficients are part of the lag polynomial on
            the right-hand-side of the ARMA definition (i.e. they have the same
            sign from the usual econometrics convention in which the coefficients
            are on the right-hand-side of the ARMA definition).
        arma_acovf : ndarray
            The vector of autocovariances of the ARMA process.
    
        Returns
        -------
        acovf : ndarray
            A matrix containing the autocovariances of the portion of the
            transformed process with time-varying autocovariances. Its dimension
            is equal to `min(m * 2, n)` where `m = max(len(ar) - 1, len(ma) - 1)`
            and `n` is the length of the input array `arma_acovf`. It is important
            to note that only the values in the first `m` columns or `m` rows are
            valid. In particular, the entries in the block `acovf[m:, m:]` should
            not be used in any case (and in fact will always be equal to zeros).
        acovf2 : ndarray
            An array containing the autocovariance function of the portion of the
            transformed process with time-invariant autocovariances. Its dimension
            is equal to `max(n - m, 0)` where `n` is the length of the input
            array `arma_acovf`.
    
        Notes
        -----
        The definition of this autocovariance matrix is from _[1] equation 3.3.3.
    
        This function assumes that the variance of the ARMA innovation term is
        equal to one. If this is not true, then the calling program should replace
        `arma_acovf` with `arma_acovf / sigma2`, where sigma2 is that variance.
    
        This function is relatively fast even when `arma_acovf` is large, since
        it only constructs the full autocovariance matrix for a generally small
        subset of observations. The trade-off is that the output of this function
        is somewhat more difficult to use.
    
        References
        ----------
        .. [1] Brockwell, Peter J., and Richard A. Davis. 2009.
           Time Series: Theory and Methods. 2nd ed. 1991.
           New York, NY: Springer.
    """
    pass

def __pyx_unpickle_Enum(*args, **kwargs): # real signature unknown
    pass

# no classes
# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x00000208F0F62E80>'

__spec__ = None # (!) real value is "ModuleSpec(name='statsmodels.tsa.innovations._arma_innovations', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x00000208F0F62E80>, origin='C:\\\\Users\\\\Doly\\\\Anaconda3\\\\lib\\\\site-packages\\\\statsmodels\\\\tsa\\\\innovations\\\\_arma_innovations.cp37-win_amd64.pyd')"

__test__ = {}

