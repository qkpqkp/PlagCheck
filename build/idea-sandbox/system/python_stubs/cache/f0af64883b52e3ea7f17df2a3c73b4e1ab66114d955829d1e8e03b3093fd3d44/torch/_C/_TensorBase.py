# encoding: utf-8
# module torch._C
# from C:\Users\Doly\Anaconda3\lib\site-packages\torch\_C.cp37-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import torch._C._onnx as _onnx # <module 'torch._C._onnx'>
import torch._C._jit_tree_views as _jit_tree_views # <module 'torch._C._jit_tree_views'>
import torch._C._nn as _nn # <module 'torch._C._nn'>
import torch._C.cpp as cpp # <module 'torch._C.cpp'>
import torch._C._functions as _functions # <module 'torch._C._functions'>
import pybind11_builtins as __pybind11_builtins


from .object import object

class _TensorBase(object):
    # no doc
    def abs(self): # real signature unknown; restored from __doc__
        """
        abs() -> Tensor
        
        See :func:`torch.abs`
        """
        pass

    def abs_(self): # real signature unknown; restored from __doc__
        """
        abs_() -> Tensor
        
        In-place version of :meth:`~Tensor.abs`
        """
        pass

    def acos(self): # real signature unknown; restored from __doc__
        """
        acos() -> Tensor
        
        See :func:`torch.acos`
        """
        pass

    def acos_(self): # real signature unknown; restored from __doc__
        """
        acos_() -> Tensor
        
        In-place version of :meth:`~Tensor.acos`
        """
        pass

    def add(self, value): # real signature unknown; restored from __doc__
        """
        add(value) -> Tensor
        add(value=1, other) -> Tensor
        
        See :func:`torch.add`
        """
        pass

    def addbmm(self, beta=1, alpha=1, batch1, batch2): # real signature unknown; restored from __doc__
        """
        addbmm(beta=1, alpha=1, batch1, batch2) -> Tensor
        
        See :func:`torch.addbmm`
        """
        pass

    def addbmm_(self, beta=1, alpha=1, batch1, batch2): # real signature unknown; restored from __doc__
        """
        addbmm_(beta=1, alpha=1, batch1, batch2) -> Tensor
        
        In-place version of :meth:`~Tensor.addbmm`
        """
        pass

    def addcdiv(self, value=1, tensor1, tensor2): # real signature unknown; restored from __doc__
        """
        addcdiv(value=1, tensor1, tensor2) -> Tensor
        
        See :func:`torch.addcdiv`
        """
        pass

    def addcdiv_(self, value=1, tensor1, tensor2): # real signature unknown; restored from __doc__
        """
        addcdiv_(value=1, tensor1, tensor2) -> Tensor
        
        In-place version of :meth:`~Tensor.addcdiv`
        """
        pass

    def addcmul(self, value=1, tensor1, tensor2): # real signature unknown; restored from __doc__
        """
        addcmul(value=1, tensor1, tensor2) -> Tensor
        
        See :func:`torch.addcmul`
        """
        pass

    def addcmul_(self, value=1, tensor1, tensor2): # real signature unknown; restored from __doc__
        """
        addcmul_(value=1, tensor1, tensor2) -> Tensor
        
        In-place version of :meth:`~Tensor.addcmul`
        """
        pass

    def addmm(self, beta=1, alpha=1, mat1, mat2): # real signature unknown; restored from __doc__
        """
        addmm(beta=1, alpha=1, mat1, mat2) -> Tensor
        
        See :func:`torch.addmm`
        """
        pass

    def addmm_(self, beta=1, alpha=1, mat1, mat2): # real signature unknown; restored from __doc__
        """
        addmm_(beta=1, alpha=1, mat1, mat2) -> Tensor
        
        In-place version of :meth:`~Tensor.addmm`
        """
        pass

    def addmv(self, beta=1, alpha=1, mat, vec): # real signature unknown; restored from __doc__
        """
        addmv(beta=1, alpha=1, mat, vec) -> Tensor
        
        See :func:`torch.addmv`
        """
        pass

    def addmv_(self, beta=1, alpha=1, mat, vec): # real signature unknown; restored from __doc__
        """
        addmv_(beta=1, alpha=1, mat, vec) -> Tensor
        
        In-place version of :meth:`~Tensor.addmv`
        """
        pass

    def addr(self, beta=1, alpha=1, vec1, vec2): # real signature unknown; restored from __doc__
        """
        addr(beta=1, alpha=1, vec1, vec2) -> Tensor
        
        See :func:`torch.addr`
        """
        pass

    def addr_(self, beta=1, alpha=1, vec1, vec2): # real signature unknown; restored from __doc__
        """
        addr_(beta=1, alpha=1, vec1, vec2) -> Tensor
        
        In-place version of :meth:`~Tensor.addr`
        """
        pass

    def add_(self, value): # real signature unknown; restored from __doc__
        """
        add_(value) -> Tensor
        add_(value=1, other) -> Tensor
        
        In-place version of :meth:`~Tensor.add`
        """
        pass

    def align_as(self, other): # real signature unknown; restored from __doc__
        """
        align_as(other) -> Tensor
        
        Permutes the dimensions of the :attr:`self` tensor to match the dimension order
        in the :attr:`other` tensor, adding size-one dims for any new names.
        
        This operation is useful for explicit broadcasting by names (see examples).
        
        All of the dims of :attr:`self` must be named in order to use this method.
        The resulting tensor is a view on the original tensor.
        
        All dimension names of :attr:`self` must be present in ``other.names``.
        :attr:`other` may contain named dimensions that are not in ``self.names``;
        the output tensor has a size-one dimension for each of those new names.
        
        To align a tensor to a specific order, use :meth:`~Tensor.align_to`.
        
        Examples::
        
            # Example 1: Applying a mask
            >>> mask = torch.randint(2, [127, 128], dtype=torch.bool).refine_names('W', 'H')
            >>> imgs = torch.randn(32, 128, 127, 3, names=('N', 'H', 'W', 'C'))
            >>> imgs.masked_fill_(mask.align_as(imgs), 0)
        
        
            # Example 2: Applying a per-channel-scale
            def scale_channels(input, scale):
                scale = scale.refine_names('C')
                return input * scale.align_as(input)
        
            >>> num_channels = 3
            >>> scale = torch.randn(num_channels, names='C')
            >>> imgs = torch.rand(32, 128, 128, num_channels, names=('N', 'H', 'W', 'C'))
            >>> more_imgs = torch.rand(32, num_channels, 128, 128, names=('N', 'C', 'H', 'W'))
            >>> videos = torch.randn(3, num_channels, 128, 128, 128, names=('N', 'C', 'H', 'W', 'D'))
        
            # scale_channels is agnostic to the dimension order of the input
            >>> scale_channels(imgs, scale)
            >>> scale_channels(more_imgs, scale)
            >>> scale_channels(videos, scale)
        
        .. warning::
            The named tensor API is experimental and subject to change.
        """
        pass

    def align_to(self, *args, **kwargs): # real signature unknown
        pass

    def all(self): # real signature unknown; restored from __doc__
        """
        .. function:: all() -> bool
        
        Returns True if all elements in the tensor are True, False otherwise.
        
        Example::
        
            >>> a = torch.rand(1, 2).bool()
            >>> a
            tensor([[False, True]], dtype=torch.bool)
            >>> a.all()
            tensor(False, dtype=torch.bool)
        
        .. function:: all(dim, keepdim=False, out=None) -> Tensor
        
        Returns True if all elements in each row of the tensor in the given
        dimension :attr:`dim` are True, False otherwise.
        
        If :attr:`keepdim` is ``True``, the output tensor is of the same size as
        :attr:`input` except in the dimension :attr:`dim` where it is of size 1.
        Otherwise, :attr:`dim` is squeezed (see :func:`torch.squeeze`), resulting
        in the output tensor having 1 fewer dimension than :attr:`input`.
        
        Args:
            dim (int): the dimension to reduce
            keepdim (bool): whether the output tensor has :attr:`dim` retained or not
            out (Tensor, optional): the output tensor
        
        Example::
        
            >>> a = torch.rand(4, 2).bool()
            >>> a
            tensor([[True, True],
                    [True, False],
                    [True, True],
                    [True, True]], dtype=torch.bool)
            >>> a.all(dim=1)
            tensor([ True, False,  True,  True], dtype=torch.bool)
            >>> a.all(dim=0)
            tensor([ True, False], dtype=torch.bool)
        """
        return False

    def allclose(self, other, rtol=1, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        allclose(other, rtol=1e-05, atol=1e-08, equal_nan=False) -> Tensor
        
        See :func:`torch.allclose`
        """
        pass

    def any(self): # real signature unknown; restored from __doc__
        """
        .. function:: any() -> bool
        
        Returns True if any elements in the tensor are True, False otherwise.
        
        Example::
        
            >>> a = torch.rand(1, 2).bool()
            >>> a
            tensor([[False, True]], dtype=torch.bool)
            >>> a.any()
            tensor(True, dtype=torch.bool)
        .. function:: any(dim, keepdim=False, out=None) -> Tensor
        
        Returns True if any elements in each row of the tensor in the given
        dimension :attr:`dim` are True, False otherwise.
        
        If :attr:`keepdim` is ``True``, the output tensor is of the same size as
        :attr:`input` except in the dimension :attr:`dim` where it is of size 1.
        Otherwise, :attr:`dim` is squeezed (see :func:`torch.squeeze`), resulting
        in the output tensor having 1 fewer dimension than :attr:`input`.
        
        Args:
            dim (int): the dimension to reduce
            keepdim (bool): whether the output tensor has :attr:`dim` retained or not
            out (Tensor, optional): the output tensor
        
        Example::
        
            >>> a = torch.randn(4, 2) < 0
            >>> a
            tensor([[ True,  True],
                    [False,  True],
                    [ True,  True],
                    [False, False]])
            >>> a.any(1)
            tensor([ True,  True,  True, False])
            >>> a.any(0)
            tensor([True, True])
        """
        return False

    def apply_(self, callable): # real signature unknown; restored from __doc__
        """
        apply_(callable) -> Tensor
        
        Applies the function :attr:`callable` to each element in the tensor, replacing
        each element with the value returned by :attr:`callable`.
        
        .. note::
        
            This function only works with CPU tensors and should not be used in code
            sections that require high performance.
        """
        pass

    def argmax(self, dim=None, keepdim=False): # real signature unknown; restored from __doc__
        """
        argmax(dim=None, keepdim=False) -> LongTensor
        
        See :func:`torch.argmax`
        """
        pass

    def argmin(self, dim=None, keepdim=False): # real signature unknown; restored from __doc__
        """
        argmin(dim=None, keepdim=False) -> LongTensor
        
        See :func:`torch.argmin`
        """
        pass

    def argsort(self, dim=-1, descending=False): # real signature unknown; restored from __doc__
        """
        argsort(dim=-1, descending=False) -> LongTensor
        
        See :func: `torch.argsort`
        """
        pass

    def asin(self): # real signature unknown; restored from __doc__
        """
        asin() -> Tensor
        
        See :func:`torch.asin`
        """
        pass

    def asin_(self): # real signature unknown; restored from __doc__
        """
        asin_() -> Tensor
        
        In-place version of :meth:`~Tensor.asin`
        """
        pass

    def as_strided(self, size, stride, storage_offset=0): # real signature unknown; restored from __doc__
        """
        as_strided(size, stride, storage_offset=0) -> Tensor
        
        See :func:`torch.as_strided`
        """
        pass

    def as_strided_(self, *args, **kwargs): # real signature unknown
        pass

    def atan(self): # real signature unknown; restored from __doc__
        """
        atan() -> Tensor
        
        See :func:`torch.atan`
        """
        pass

    def atan2(self, other): # real signature unknown; restored from __doc__
        """
        atan2(other) -> Tensor
        
        See :func:`torch.atan2`
        """
        pass

    def atan2_(self, other): # real signature unknown; restored from __doc__
        """
        atan2_(other) -> Tensor
        
        In-place version of :meth:`~Tensor.atan2`
        """
        pass

    def atan_(self): # real signature unknown; restored from __doc__
        """
        atan_() -> Tensor
        
        In-place version of :meth:`~Tensor.atan`
        """
        pass

    def backward(self, *args, **kwargs): # real signature unknown
        pass

    def baddbmm(self, beta=1, alpha=1, batch1, batch2): # real signature unknown; restored from __doc__
        """
        baddbmm(beta=1, alpha=1, batch1, batch2) -> Tensor
        
        See :func:`torch.baddbmm`
        """
        pass

    def baddbmm_(self, beta=1, alpha=1, batch1, batch2): # real signature unknown; restored from __doc__
        """
        baddbmm_(beta=1, alpha=1, batch1, batch2) -> Tensor
        
        In-place version of :meth:`~Tensor.baddbmm`
        """
        pass

    def bernoulli(self, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        bernoulli(*, generator=None) -> Tensor
        
        Returns a result tensor where each :math:`\texttt{result[i]}` is independently
        sampled from :math:`\text{Bernoulli}(\texttt{self[i]})`. :attr:`self` must have
        floating point ``dtype``, and the result will have the same ``dtype``.
        
        See :func:`torch.bernoulli`
        """
        pass

    def bernoulli_(self, p=0.5, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        .. function:: bernoulli_(p=0.5, *, generator=None) -> Tensor
        
            Fills each location of :attr:`self` with an independent sample from
            :math:`\text{Bernoulli}(\texttt{p})`. :attr:`self` can have integral
            ``dtype``.
        
        .. function:: bernoulli_(p_tensor, *, generator=None) -> Tensor
        
            :attr:`p_tensor` should be a tensor containing probabilities to be used for
            drawing the binary random number.
        
            The :math:`\text{i}^{th}` element of :attr:`self` tensor will be set to a
            value sampled from :math:`\text{Bernoulli}(\texttt{p\_tensor[i]})`.
        
            :attr:`self` can have integral ``dtype``, but :attr:`p_tensor` must have
            floating point ``dtype``.
        
        See also :meth:`~Tensor.bernoulli` and :func:`torch.bernoulli`
        """
        pass

    def bfloat16(self): # real signature unknown; restored from __doc__
        """
        bfloat16() -> Tensor
        ``self.bfloat16()`` is equivalent to ``self.to(torch.bfloat16)``. See :func:`to`.
        """
        pass

    def bincount(self, weights=None, minlength=0): # real signature unknown; restored from __doc__
        """
        bincount(weights=None, minlength=0) -> Tensor
        
        See :func:`torch.bincount`
        """
        pass

    def bitwise_not(self): # real signature unknown; restored from __doc__
        """
        bitwise_not() -> Tensor
        
        See :func:`torch.bitwise_not`
        """
        pass

    def bitwise_not_(self): # real signature unknown; restored from __doc__
        """
        bitwise_not_() -> Tensor
        
        In-place version of :meth:`~Tensor.bitwise_not`
        """
        pass

    def bmm(self, batch2): # real signature unknown; restored from __doc__
        """
        bmm(batch2) -> Tensor
        
        See :func:`torch.bmm`
        """
        pass

    def bool(self): # real signature unknown; restored from __doc__
        """
        bool() -> Tensor
        
        ``self.bool()`` is equivalent to ``self.to(torch.bool)``. See :func:`to`.
        """
        pass

    def byte(self): # real signature unknown; restored from __doc__
        """
        byte() -> Tensor
        
        ``self.byte()`` is equivalent to ``self.to(torch.uint8)``. See :func:`to`.
        """
        pass

    def cauchy_(self, median=0, sigma=1, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        cauchy_(median=0, sigma=1, *, generator=None) -> Tensor
        
        Fills the tensor with numbers drawn from the Cauchy distribution:
        
        .. math::
        
            f(x) = \dfrac{1}{\pi} \dfrac{\sigma}{(x - \text{median})^2 + \sigma^2}
        """
        pass

    def ceil(self): # real signature unknown; restored from __doc__
        """
        ceil() -> Tensor
        
        See :func:`torch.ceil`
        """
        pass

    def ceil_(self): # real signature unknown; restored from __doc__
        """
        ceil_() -> Tensor
        
        In-place version of :meth:`~Tensor.ceil`
        """
        pass

    def char(self): # real signature unknown; restored from __doc__
        """
        char() -> Tensor
        
        ``self.char()`` is equivalent to ``self.to(torch.int8)``. See :func:`to`.
        """
        pass

    def cholesky(self, upper=False): # real signature unknown; restored from __doc__
        """
        cholesky(upper=False) -> Tensor
        
        See :func:`torch.cholesky`
        """
        pass

    def cholesky_inverse(self, upper=False): # real signature unknown; restored from __doc__
        """
        cholesky_inverse(upper=False) -> Tensor
        
        See :func:`torch.cholesky_inverse`
        """
        pass

    def cholesky_solve(self, input2, upper=False): # real signature unknown; restored from __doc__
        """
        cholesky_solve(input2, upper=False) -> Tensor
        
        See :func:`torch.cholesky_solve`
        """
        pass

    def chunk(self, chunks, dim=0): # real signature unknown; restored from __doc__
        """
        chunk(chunks, dim=0) -> List of Tensors
        
        See :func:`torch.chunk`
        """
        return []

    def clamp(self, min, max): # real signature unknown; restored from __doc__
        """
        clamp(min, max) -> Tensor
        
        See :func:`torch.clamp`
        """
        pass

    def clamp_(self, min, max): # real signature unknown; restored from __doc__
        """
        clamp_(min, max) -> Tensor
        
        In-place version of :meth:`~Tensor.clamp`
        """
        pass

    def clamp_max(self, *args, **kwargs): # real signature unknown
        pass

    def clamp_max_(self, *args, **kwargs): # real signature unknown
        pass

    def clamp_min(self, *args, **kwargs): # real signature unknown
        pass

    def clamp_min_(self, *args, **kwargs): # real signature unknown
        pass

    def clone(self): # real signature unknown; restored from __doc__
        """
        clone() -> Tensor
        
        Returns a copy of the :attr:`self` tensor. The copy has the same size and data
        type as :attr:`self`.
        
        .. note::
        
            Unlike `copy_()`, this function is recorded in the computation graph. Gradients
            propagating to the cloned tensor will propagate to the original tensor.
        """
        pass

    def coalesce(self, *args, **kwargs): # real signature unknown
        pass

    def contiguous(self): # real signature unknown; restored from __doc__
        """
        contiguous() -> Tensor
        
        Returns a contiguous tensor containing the same data as :attr:`self` tensor. If
        :attr:`self` tensor is contiguous, this function returns the :attr:`self`
        tensor.
        """
        pass

    def copy_(self, src, non_blocking=False): # real signature unknown; restored from __doc__
        """
        copy_(src, non_blocking=False) -> Tensor
        
        Copies the elements from :attr:`src` into :attr:`self` tensor and returns
        :attr:`self`.
        
        The :attr:`src` tensor must be :ref:`broadcastable <broadcasting-semantics>`
        with the :attr:`self` tensor. It may be of a different data type or reside on a
        different device.
        
        Args:
            src (Tensor): the source tensor to copy from
            non_blocking (bool): if ``True`` and this copy is between CPU and GPU,
                the copy may occur asynchronously with respect to the host. For other
                cases, this argument has no effect.
        """
        pass

    def cos(self): # real signature unknown; restored from __doc__
        """
        cos() -> Tensor
        
        See :func:`torch.cos`
        """
        pass

    def cosh(self): # real signature unknown; restored from __doc__
        """
        cosh() -> Tensor
        
        See :func:`torch.cosh`
        """
        pass

    def cosh_(self): # real signature unknown; restored from __doc__
        """
        cosh_() -> Tensor
        
        In-place version of :meth:`~Tensor.cosh`
        """
        pass

    def cos_(self): # real signature unknown; restored from __doc__
        """
        cos_() -> Tensor
        
        In-place version of :meth:`~Tensor.cos`
        """
        pass

    def cpu(self): # real signature unknown; restored from __doc__
        """
        cpu() -> Tensor
        
        Returns a copy of this object in CPU memory.
        
        If this object is already in CPU memory and on the correct device,
        then no copy is performed and the original object is returned.
        """
        pass

    def cross(self, other, dim=-1): # real signature unknown; restored from __doc__
        """
        cross(other, dim=-1) -> Tensor
        
        See :func:`torch.cross`
        """
        pass

    def cuda(self, device=None, non_blocking=False): # real signature unknown; restored from __doc__
        """
        cuda(device=None, non_blocking=False) -> Tensor
        
        Returns a copy of this object in CUDA memory.
        
        If this object is already in CUDA memory and on the correct device,
        then no copy is performed and the original object is returned.
        
        Args:
            device (:class:`torch.device`): The destination GPU device.
                Defaults to the current CUDA device.
            non_blocking (bool): If ``True`` and the source is in pinned memory,
                the copy will be asynchronous with respect to the host.
                Otherwise, the argument has no effect. Default: ``False``.
        """
        pass

    def cumprod(self, dim, dtype=None): # real signature unknown; restored from __doc__
        """
        cumprod(dim, dtype=None) -> Tensor
        
        See :func:`torch.cumprod`
        """
        pass

    def cumsum(self, dim, dtype=None): # real signature unknown; restored from __doc__
        """
        cumsum(dim, dtype=None) -> Tensor
        
        See :func:`torch.cumsum`
        """
        pass

    def data_ptr(self): # real signature unknown; restored from __doc__
        """
        data_ptr() -> int
        
        Returns the address of the first element of :attr:`self` tensor.
        """
        return 0

    def dense_dim(self): # real signature unknown; restored from __doc__
        """
        dense_dim() -> int
        
        If :attr:`self` is a sparse COO tensor (i.e., with ``torch.sparse_coo`` layout),
        this returns the number of dense dimensions. Otherwise, this throws an error.
        
        See also :meth:`Tensor.sparse_dim`.
        """
        return 0

    def dequantize(self): # real signature unknown; restored from __doc__
        """
        dequantize() -> Tensor
        
        Given a quantized Tensor, dequantize it and return the dequantized float Tensor.
        """
        pass

    def det(self): # real signature unknown; restored from __doc__
        """
        det() -> Tensor
        
        See :func:`torch.det`
        """
        pass

    def detach(self, *args, **kwargs): # real signature unknown
        """
        Returns a new Tensor, detached from the current graph.
        
            The result will never require gradient.
        
            .. note::
        
              Returned Tensor shares the same storage with the original one.
              In-place modifications on either of them will be seen, and may trigger
              errors in correctness checks.
              IMPORTANT NOTE: Previously, in-place size / stride / storage changes
              (such as `resize_` / `resize_as_` / `set_` / `transpose_`) to the returned tensor
              also update the original tensor. Now, these in-place changes will not update the
              original tensor anymore, and will instead trigger an error.
              For sparse tensors:
              In-place indices / values changes (such as `zero_` / `copy_` / `add_`) to the
              returned tensor will not update the original tensor anymore, and will instead
              trigger an error.
        """
        pass

    def detach_(self, *args, **kwargs): # real signature unknown
        """
        Detaches the Tensor from the graph that created it, making it a leaf.
            Views cannot be detached in-place.
        """
        pass

    def diag(self, diagonal=0): # real signature unknown; restored from __doc__
        """
        diag(diagonal=0) -> Tensor
        
        See :func:`torch.diag`
        """
        pass

    def diagflat(self, offset=0): # real signature unknown; restored from __doc__
        """
        diagflat(offset=0) -> Tensor
        
        See :func:`torch.diagflat`
        """
        pass

    def diagonal(self, offset=0, dim1=0, dim2=1): # real signature unknown; restored from __doc__
        """
        diagonal(offset=0, dim1=0, dim2=1) -> Tensor
        
        See :func:`torch.diagonal`
        """
        pass

    def diag_embed(self, offset=0, dim1=-2, dim2=-1): # real signature unknown; restored from __doc__
        """
        diag_embed(offset=0, dim1=-2, dim2=-1) -> Tensor
        
        See :func:`torch.diag_embed`
        """
        pass

    def digamma(self): # real signature unknown; restored from __doc__
        """
        digamma() -> Tensor
        
        See :func:`torch.digamma`
        """
        pass

    def digamma_(self): # real signature unknown; restored from __doc__
        """
        digamma_() -> Tensor
        
        In-place version of :meth:`~Tensor.digamma`
        """
        pass

    def dim(self): # real signature unknown; restored from __doc__
        """
        dim() -> int
        
        Returns the number of dimensions of :attr:`self` tensor.
        """
        return 0

    def dist(self, other, p=2): # real signature unknown; restored from __doc__
        """
        dist(other, p=2) -> Tensor
        
        See :func:`torch.dist`
        """
        pass

    def div(self, value): # real signature unknown; restored from __doc__
        """
        div(value) -> Tensor
        
        See :func:`torch.div`
        """
        pass

    def div_(self, value): # real signature unknown; restored from __doc__
        """
        div_(value) -> Tensor
        
        In-place version of :meth:`~Tensor.div`
        """
        pass

    def dot(self, tensor2): # real signature unknown; restored from __doc__
        """
        dot(tensor2) -> Tensor
        
        See :func:`torch.dot`
        """
        pass

    def double(self): # real signature unknown; restored from __doc__
        """
        double() -> Tensor
        
        ``self.double()`` is equivalent to ``self.to(torch.float64)``. See :func:`to`.
        """
        pass

    def eig(self, eigenvectors=False): # real signature unknown; restored from __doc__
        """
        eig(eigenvectors=False) -> (Tensor, Tensor)
        
        See :func:`torch.eig`
        """
        pass

    def element_size(self): # real signature unknown; restored from __doc__
        """
        element_size() -> int
        
        Returns the size in bytes of an individual element.
        
        Example::
        
            >>> torch.tensor([]).element_size()
            4
            >>> torch.tensor([], dtype=torch.uint8).element_size()
            1
        """
        return 0

    def eq(self, other): # real signature unknown; restored from __doc__
        """
        eq(other) -> Tensor
        
        See :func:`torch.eq`
        """
        pass

    def equal(self, other): # real signature unknown; restored from __doc__
        """
        equal(other) -> bool
        
        See :func:`torch.equal`
        """
        return False

    def eq_(self, other): # real signature unknown; restored from __doc__
        """
        eq_(other) -> Tensor
        
        In-place version of :meth:`~Tensor.eq`
        """
        pass

    def erf(self): # real signature unknown; restored from __doc__
        """
        erf() -> Tensor
        
        See :func:`torch.erf`
        """
        pass

    def erfc(self): # real signature unknown; restored from __doc__
        """
        erfc() -> Tensor
        
        See :func:`torch.erfc`
        """
        pass

    def erfc_(self): # real signature unknown; restored from __doc__
        """
        erfc_() -> Tensor
        
        In-place version of :meth:`~Tensor.erfc`
        """
        pass

    def erfinv(self): # real signature unknown; restored from __doc__
        """
        erfinv() -> Tensor
        
        See :func:`torch.erfinv`
        """
        pass

    def erfinv_(self): # real signature unknown; restored from __doc__
        """
        erfinv_() -> Tensor
        
        In-place version of :meth:`~Tensor.erfinv`
        """
        pass

    def erf_(self): # real signature unknown; restored from __doc__
        """
        erf_() -> Tensor
        
        In-place version of :meth:`~Tensor.erf`
        """
        pass

    def exp(self): # real signature unknown; restored from __doc__
        """
        exp() -> Tensor
        
        See :func:`torch.exp`
        """
        pass

    def expand(self, *sizes): # real signature unknown; restored from __doc__
        """
        expand(*sizes) -> Tensor
        
        Returns a new view of the :attr:`self` tensor with singleton dimensions expanded
        to a larger size.
        
        Passing -1 as the size for a dimension means not changing the size of
        that dimension.
        
        Tensor can be also expanded to a larger number of dimensions, and the
        new ones will be appended at the front. For the new dimensions, the
        size cannot be set to -1.
        
        Expanding a tensor does not allocate new memory, but only creates a
        new view on the existing tensor where a dimension of size one is
        expanded to a larger size by setting the ``stride`` to 0. Any dimension
        of size 1 can be expanded to an arbitrary value without allocating new
        memory.
        
        Args:
            *sizes (torch.Size or int...): the desired expanded size
        
        .. warning::
        
            More than one element of an expanded tensor may refer to a single
            memory location. As a result, in-place operations (especially ones that
            are vectorized) may result in incorrect behavior. If you need to write
            to the tensors, please clone them first.
        
        Example::
        
            >>> x = torch.tensor([[1], [2], [3]])
            >>> x.size()
            torch.Size([3, 1])
            >>> x.expand(3, 4)
            tensor([[ 1,  1,  1,  1],
                    [ 2,  2,  2,  2],
                    [ 3,  3,  3,  3]])
            >>> x.expand(-1, 4)   # -1 means not changing the size of that dimension
            tensor([[ 1,  1,  1,  1],
                    [ 2,  2,  2,  2],
                    [ 3,  3,  3,  3]])
        """
        pass

    def expand_as(self, other): # real signature unknown; restored from __doc__
        """
        expand_as(other) -> Tensor
        
        Expand this tensor to the same size as :attr:`other`.
        ``self.expand_as(other)`` is equivalent to ``self.expand(other.size())``.
        
        Please see :meth:`~Tensor.expand` for more information about ``expand``.
        
        Args:
            other (:class:`torch.Tensor`): The result tensor has the same size
                as :attr:`other`.
        """
        pass

    def expm1(self): # real signature unknown; restored from __doc__
        """
        expm1() -> Tensor
        
        See :func:`torch.expm1`
        """
        pass

    def expm1_(self): # real signature unknown; restored from __doc__
        """
        expm1_() -> Tensor
        
        In-place version of :meth:`~Tensor.expm1`
        """
        pass

    def exponential_(self, lambd=1, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        exponential_(lambd=1, *, generator=None) -> Tensor
        
        Fills :attr:`self` tensor with elements drawn from the exponential distribution:
        
        .. math::
        
            f(x) = \lambda e^{-\lambda x}
        """
        pass

    def exp_(self): # real signature unknown; restored from __doc__
        """
        exp_() -> Tensor
        
        In-place version of :meth:`~Tensor.exp`
        """
        pass

    def fft(self, signal_ndim, normalized=False): # real signature unknown; restored from __doc__
        """
        fft(signal_ndim, normalized=False) -> Tensor
        
        See :func:`torch.fft`
        """
        pass

    def fill_(self, value): # real signature unknown; restored from __doc__
        """
        fill_(value) -> Tensor
        
        Fills :attr:`self` tensor with the specified value.
        """
        pass

    def fill_diagonal_(self, fill_value, wrap=False): # real signature unknown; restored from __doc__
        """
        fill_diagonal_(fill_value, wrap=False) -> Tensor
        
        Fill the main diagonal of a tensor that has at least 2-dimensions.
        When dims>2, all dimensions of input must be of equal length.
        This function modifies the input tensor in-place, and returns the input tensor.
        
        Arguments:
            fill_value (Scalar): the fill value
            wrap (bool): the diagonal 'wrapped' after N columns for tall matrices.
        
        Example::
        
            >>> a = torch.zeros(3, 3)
            >>> a.fill_diagonal_(5)
            tensor([[5., 0., 0.],
                    [0., 5., 0.],
                    [0., 0., 5.]])
            >>> b = torch.zeros(7, 3)
            >>> b.fill_diagonal_(5)
            tensor([[5., 0., 0.],
                    [0., 5., 0.],
                    [0., 0., 5.],
                    [0., 0., 0.],
                    [0., 0., 0.],
                    [0., 0., 0.],
                    [0., 0., 0.]])
            >>> c = torch.zeros(7, 3)
            >>> c.fill_diagonal_(5, wrap=True)
            tensor([[5., 0., 0.],
                    [0., 5., 0.],
                    [0., 0., 5.],
                    [0., 0., 0.],
                    [5., 0., 0.],
                    [0., 5., 0.],
                    [0., 0., 5.]])
        """
        pass

    def flatten(self, input, start_dim=0, end_dim=-1): # real signature unknown; restored from __doc__
        """
        flatten(input, start_dim=0, end_dim=-1) -> Tensor
        
        see :func:`torch.flatten`
        """
        pass

    def flip(self, dims): # real signature unknown; restored from __doc__
        """
        flip(dims) -> Tensor
        
        See :func:`torch.flip`
        """
        pass

    def float(self): # real signature unknown; restored from __doc__
        """
        float() -> Tensor
        
        ``self.float()`` is equivalent to ``self.to(torch.float32)``. See :func:`to`.
        """
        pass

    def floor(self): # real signature unknown; restored from __doc__
        """
        floor() -> Tensor
        
        See :func:`torch.floor`
        """
        pass

    def floor_(self): # real signature unknown; restored from __doc__
        """
        floor_() -> Tensor
        
        In-place version of :meth:`~Tensor.floor`
        """
        pass

    def fmod(self, divisor): # real signature unknown; restored from __doc__
        """
        fmod(divisor) -> Tensor
        
        See :func:`torch.fmod`
        """
        pass

    def fmod_(self, divisor): # real signature unknown; restored from __doc__
        """
        fmod_(divisor) -> Tensor
        
        In-place version of :meth:`~Tensor.fmod`
        """
        pass

    def frac(self): # real signature unknown; restored from __doc__
        """
        frac() -> Tensor
        
        See :func:`torch.frac`
        """
        pass

    def frac_(self): # real signature unknown; restored from __doc__
        """
        frac_() -> Tensor
        
        In-place version of :meth:`~Tensor.frac`
        """
        pass

    def gather(self, dim, index): # real signature unknown; restored from __doc__
        """
        gather(dim, index) -> Tensor
        
        See :func:`torch.gather`
        """
        pass

    def ge(self, other): # real signature unknown; restored from __doc__
        """
        ge(other) -> Tensor
        
        See :func:`torch.ge`
        """
        pass

    def geometric_(self, p, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        geometric_(p, *, generator=None) -> Tensor
        
        Fills :attr:`self` tensor with elements drawn from the geometric distribution:
        
        .. math::
        
            f(X=k) = p^{k - 1} (1 - p)
        """
        pass

    def geqrf(self): # real signature unknown; restored from __doc__
        """
        geqrf() -> (Tensor, Tensor)
        
        See :func:`torch.geqrf`
        """
        pass

    def ger(self, vec2): # real signature unknown; restored from __doc__
        """
        ger(vec2) -> Tensor
        
        See :func:`torch.ger`
        """
        pass

    def get_device(self): # real signature unknown; restored from __doc__
        """
        get_device() -> Device ordinal (Integer)
        
        For CUDA tensors, this function returns the device ordinal of the GPU on which the tensor resides.
        For CPU tensors, an error is thrown.
        
        Example::
        
            >>> x = torch.randn(3, 4, 5, device='cuda:0')
            >>> x.get_device()
            0
            >>> x.cpu().get_device()  # RuntimeError: get_device is not implemented for type torch.FloatTensor
        """
        pass

    def ge_(self, other): # real signature unknown; restored from __doc__
        """
        ge_(other) -> Tensor
        
        In-place version of :meth:`~Tensor.ge`
        """
        pass

    def gt(self, other): # real signature unknown; restored from __doc__
        """
        gt(other) -> Tensor
        
        See :func:`torch.gt`
        """
        pass

    def gt_(self, other): # real signature unknown; restored from __doc__
        """
        gt_(other) -> Tensor
        
        In-place version of :meth:`~Tensor.gt`
        """
        pass

    def half(self): # real signature unknown; restored from __doc__
        """
        half() -> Tensor
        
        ``self.half()`` is equivalent to ``self.to(torch.float16)``. See :func:`to`.
        """
        pass

    def hardshrink(self, lambd=0.5): # real signature unknown; restored from __doc__
        """
        hardshrink(lambd=0.5) -> Tensor
        
        See :func:`torch.nn.functional.hardshrink`
        """
        pass

    def has_names(self, *args, **kwargs): # real signature unknown
        """ Is ``True`` if any of this tensor's dimensions are named. Otherwise, is ``False``. """
        pass

    def histc(self, bins=100, min=0, max=0): # real signature unknown; restored from __doc__
        """
        histc(bins=100, min=0, max=0) -> Tensor
        
        See :func:`torch.histc`
        """
        pass

    def ifft(self, signal_ndim, normalized=False): # real signature unknown; restored from __doc__
        """
        ifft(signal_ndim, normalized=False) -> Tensor
        
        See :func:`torch.ifft`
        """
        pass

    def index_add(self, dim, index, tensor): # real signature unknown; restored from __doc__
        """
        index_add(dim, index, tensor) -> Tensor
        
        Out-of-place version of :meth:`torch.Tensor.index_add_`
        """
        pass

    def index_add_(self, dim, index, tensor): # real signature unknown; restored from __doc__
        """
        index_add_(dim, index, tensor) -> Tensor
        
        Accumulate the elements of :attr:`tensor` into the :attr:`self` tensor by adding
        to the indices in the order given in :attr:`index`. For example, if ``dim == 0``
        and ``index[i] == j``, then the ``i``\ th row of :attr:`tensor` is added to the
        ``j``\ th row of :attr:`self`.
        
        The :attr:`dim`\ th dimension of :attr:`tensor` must have the same size as the
        length of :attr:`index` (which must be a vector), and all other dimensions must
        match :attr:`self`, or an error will be raised.
        
        .. include:: cuda_deterministic.rst
        
        Args:
            dim (int): dimension along which to index
            index (LongTensor): indices of :attr:`tensor` to select from
            tensor (Tensor): the tensor containing values to add
        
        Example::
        
            >>> x = torch.ones(5, 3)
            >>> t = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype=torch.float)
            >>> index = torch.tensor([0, 4, 2])
            >>> x.index_add_(0, index, t)
            tensor([[  2.,   3.,   4.],
                    [  1.,   1.,   1.],
                    [  8.,   9.,  10.],
                    [  1.,   1.,   1.],
                    [  5.,   6.,   7.]])
        """
        pass

    def index_copy(self, dim, index, tensor): # real signature unknown; restored from __doc__
        """
        index_copy(dim, index, tensor) -> Tensor
        
        Out-of-place version of :meth:`torch.Tensor.index_copy_`
        """
        pass

    def index_copy_(self, dim, index, tensor): # real signature unknown; restored from __doc__
        """
        index_copy_(dim, index, tensor) -> Tensor
        
        Copies the elements of :attr:`tensor` into the :attr:`self` tensor by selecting
        the indices in the order given in :attr:`index`. For example, if ``dim == 0``
        and ``index[i] == j``, then the ``i``\ th row of :attr:`tensor` is copied to the
        ``j``\ th row of :attr:`self`.
        
        The :attr:`dim`\ th dimension of :attr:`tensor` must have the same size as the
        length of :attr:`index` (which must be a vector), and all other dimensions must
        match :attr:`self`, or an error will be raised.
        
        Args:
            dim (int): dimension along which to index
            index (LongTensor): indices of :attr:`tensor` to select from
            tensor (Tensor): the tensor containing values to copy
        
        Example::
        
            >>> x = torch.zeros(5, 3)
            >>> t = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype=torch.float)
            >>> index = torch.tensor([0, 4, 2])
            >>> x.index_copy_(0, index, t)
            tensor([[ 1.,  2.,  3.],
                    [ 0.,  0.,  0.],
                    [ 7.,  8.,  9.],
                    [ 0.,  0.,  0.],
                    [ 4.,  5.,  6.]])
        """
        pass

    def index_fill(self, dim, index, value): # real signature unknown; restored from __doc__
        """
        index_fill(dim, index, value) -> Tensor
        
        Out-of-place version of :meth:`torch.Tensor.index_fill_`
        """
        pass

    def index_fill_(self, dim, index, val): # real signature unknown; restored from __doc__
        """
        index_fill_(dim, index, val) -> Tensor
        
        Fills the elements of the :attr:`self` tensor with value :attr:`val` by
        selecting the indices in the order given in :attr:`index`.
        
        Args:
            dim (int): dimension along which to index
            index (LongTensor): indices of :attr:`self` tensor to fill in
            val (float): the value to fill with
        
        Example::
            >>> x = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype=torch.float)
            >>> index = torch.tensor([0, 2])
            >>> x.index_fill_(1, index, -1)
            tensor([[-1.,  2., -1.],
                    [-1.,  5., -1.],
                    [-1.,  8., -1.]])
        """
        pass

    def index_put(self, indices, value, accumulate=False): # real signature unknown; restored from __doc__
        """
        index_put(indices, value, accumulate=False) -> Tensor
        
        Out-place version of :meth:`~Tensor.index_put_`
        """
        pass

    def index_put_(self, indices, value, accumulate=False): # real signature unknown; restored from __doc__
        """
        index_put_(indices, value, accumulate=False) -> Tensor
        
        Puts values from the tensor :attr:`value` into the tensor :attr:`self` using
        the indices specified in :attr:`indices` (which is a tuple of Tensors). The
        expression ``tensor.index_put_(indices, value)`` is equivalent to
        ``tensor[indices] = value``. Returns :attr:`self`.
        
        If :attr:`accumulate` is ``True``, the elements in :attr:`tensor` are added to
        :attr:`self`. If accumulate is ``False``, the behavior is undefined if indices
        contain duplicate elements.
        
        Args:
            indices (tuple of LongTensor): tensors used to index into `self`.
            value (Tensor): tensor of same dtype as `self`.
            accumulate (bool): whether to accumulate into self
        """
        pass

    def index_select(self, dim, index): # real signature unknown; restored from __doc__
        """
        index_select(dim, index) -> Tensor
        
        See :func:`torch.index_select`
        """
        pass

    def indices(self): # real signature unknown; restored from __doc__
        """
        indices() -> Tensor
        
        If :attr:`self` is a sparse COO tensor (i.e., with ``torch.sparse_coo`` layout),
        this returns a view of the contained indices tensor. Otherwise, this throws an
        error.
        
        See also :meth:`Tensor.values`.
        
        .. note::
          This method can only be called on a coalesced sparse tensor. See
          :meth:`Tensor.coalesce` for details.
        """
        pass

    def int(self): # real signature unknown; restored from __doc__
        """
        int() -> Tensor
        
        ``self.int()`` is equivalent to ``self.to(torch.int32)``. See :func:`to`.
        """
        pass

    def int_repr(self): # real signature unknown; restored from __doc__
        """
        int_repr() -> Tensor
        
        Given a quantized Tensor,
        ``self.int_repr()`` returns a CPU Tensor with uint8_t as data type that stores the
        underlying uint8_t values of the given Tensor.
        """
        pass

    def inverse(self): # real signature unknown; restored from __doc__
        """
        inverse() -> Tensor
        
        See :func:`torch.inverse`
        """
        pass

    def irfft(self, signal_ndim, normalized=False, onesided=True, signal_sizes=None): # real signature unknown; restored from __doc__
        """
        irfft(signal_ndim, normalized=False, onesided=True, signal_sizes=None) -> Tensor
        
        See :func:`torch.irfft`
        """
        pass

    def isclose(self, *args, **kwargs): # real signature unknown
        pass

    def is_coalesced(self, *args, **kwargs): # real signature unknown
        pass

    def is_complex(self, *args, **kwargs): # real signature unknown
        pass

    def is_contiguous(self): # real signature unknown; restored from __doc__
        """
        is_contiguous() -> bool
        
        Returns True if :attr:`self` tensor is contiguous in memory in C order.
        """
        return False

    def is_distributed(self, *args, **kwargs): # real signature unknown
        pass

    def is_floating_point(self): # real signature unknown; restored from __doc__
        """
        is_floating_point() -> bool
        
        Returns True if the data type of :attr:`self` is a floating point data type.
        """
        return False

    def is_nonzero(self, *args, **kwargs): # real signature unknown
        pass

    def is_pinned(self, *args, **kwargs): # real signature unknown
        """ Returns true if this tensor resides in pinned memory. """
        pass

    def is_same_size(self, *args, **kwargs): # real signature unknown
        pass

    def is_set_to(self, tensor): # real signature unknown; restored from __doc__
        """
        is_set_to(tensor) -> bool
        
        Returns True if this object refers to the same ``THTensor`` object from the
        Torch C API as the given tensor.
        """
        return False

    def is_signed(self): # real signature unknown; restored from __doc__
        """
        is_signed() -> bool
        
        Returns True if the data type of :attr:`self` is a signed data type.
        """
        return False

    def item(self): # real signature unknown; restored from __doc__
        """
        item() -> number
        
        Returns the value of this tensor as a standard Python number. This only works
        for tensors with one element. For other cases, see :meth:`~Tensor.tolist`.
        
        This operation is not differentiable.
        
        Example::
        
            >>> x = torch.tensor([1.0])
            >>> x.item()
            1.0
        """
        return 0

    def kthvalue(self, k, dim=None, keepdim=False): # real signature unknown; restored from __doc__
        """
        kthvalue(k, dim=None, keepdim=False) -> (Tensor, LongTensor)
        
        See :func:`torch.kthvalue`
        """
        pass

    def le(self, other): # real signature unknown; restored from __doc__
        """
        le(other) -> Tensor
        
        See :func:`torch.le`
        """
        pass

    def lerp(self, end, weight): # real signature unknown; restored from __doc__
        """
        lerp(end, weight) -> Tensor
        
        See :func:`torch.lerp`
        """
        pass

    def lerp_(self, end, weight): # real signature unknown; restored from __doc__
        """
        lerp_(end, weight) -> Tensor
        
        In-place version of :meth:`~Tensor.lerp`
        """
        pass

    def le_(self, other): # real signature unknown; restored from __doc__
        """
        le_(other) -> Tensor
        
        In-place version of :meth:`~Tensor.le`
        """
        pass

    def lgamma(self): # real signature unknown; restored from __doc__
        """
        lgamma() -> Tensor
        
        See :func:`torch.lgamma`
        """
        pass

    def lgamma_(self): # real signature unknown; restored from __doc__
        """
        lgamma_() -> Tensor
        
        In-place version of :meth:`~Tensor.lgamma`
        """
        pass

    def log(self): # real signature unknown; restored from __doc__
        """
        log() -> Tensor
        
        See :func:`torch.log`
        """
        pass

    def log10(self): # real signature unknown; restored from __doc__
        """
        log10() -> Tensor
        
        See :func:`torch.log10`
        """
        pass

    def log10_(self): # real signature unknown; restored from __doc__
        """
        log10_() -> Tensor
        
        In-place version of :meth:`~Tensor.log10`
        """
        pass

    def log1p(self): # real signature unknown; restored from __doc__
        """
        log1p() -> Tensor
        
        See :func:`torch.log1p`
        """
        pass

    def log1p_(self): # real signature unknown; restored from __doc__
        """
        log1p_() -> Tensor
        
        In-place version of :meth:`~Tensor.log1p`
        """
        pass

    def log2(self): # real signature unknown; restored from __doc__
        """
        log2() -> Tensor
        
        See :func:`torch.log2`
        """
        pass

    def log2_(self): # real signature unknown; restored from __doc__
        """
        log2_() -> Tensor
        
        In-place version of :meth:`~Tensor.log2`
        """
        pass

    def logdet(self): # real signature unknown; restored from __doc__
        """
        logdet() -> Tensor
        
        See :func:`torch.logdet`
        """
        pass

    def logical_not(self): # real signature unknown; restored from __doc__
        """
        logical_not() -> Tensor
        
        See :func:`torch.logical_not`
        """
        pass

    def logical_not_(self): # real signature unknown; restored from __doc__
        """
        logical_not_() -> Tensor
        
        In-place version of :meth:`~Tensor.logical_not`
        """
        pass

    def logical_xor(self): # real signature unknown; restored from __doc__
        """
        logical_xor() -> Tensor
        
        See :func:`torch.logical_xor`
        """
        pass

    def logical_xor_(self): # real signature unknown; restored from __doc__
        """
        logical_xor_() -> Tensor
        
        In-place version of :meth:`~Tensor.logical_xor`
        """
        pass

    def logsumexp(self, dim, keepdim=False): # real signature unknown; restored from __doc__
        """
        logsumexp(dim, keepdim=False) -> Tensor
        
        See :func:`torch.logsumexp`
        """
        pass

    def log_(self): # real signature unknown; restored from __doc__
        """
        log_() -> Tensor
        
        In-place version of :meth:`~Tensor.log`
        """
        pass

    def log_normal_(self, mean=1, std=2, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        log_normal_(mean=1, std=2, *, generator=None)
        
        Fills :attr:`self` tensor with numbers samples from the log-normal distribution
        parameterized by the given mean :math:`\mu` and standard deviation
        :math:`\sigma`. Note that :attr:`mean` and :attr:`std` are the mean and
        standard deviation of the underlying normal distribution, and not of the
        returned distribution:
        
        .. math::
        
            f(x) = \dfrac{1}{x \sigma \sqrt{2\pi}}\ e^{-\frac{(\ln x - \mu)^2}{2\sigma^2}}
        """
        pass

    def log_softmax(self, *args, **kwargs): # real signature unknown
        pass

    def long(self): # real signature unknown; restored from __doc__
        """
        long() -> Tensor
        
        ``self.long()`` is equivalent to ``self.to(torch.int64)``. See :func:`to`.
        """
        pass

    def lstsq(self, A): # real signature unknown; restored from __doc__
        """
        lstsq(A) -> (Tensor, Tensor)
        
        See :func:`torch.lstsq`
        """
        pass

    def lt(self, other): # real signature unknown; restored from __doc__
        """
        lt(other) -> Tensor
        
        See :func:`torch.lt`
        """
        pass

    def lt_(self, other): # real signature unknown; restored from __doc__
        """
        lt_(other) -> Tensor
        
        In-place version of :meth:`~Tensor.lt`
        """
        pass

    def lu_solve(self, LU_data, LU_pivots): # real signature unknown; restored from __doc__
        """
        lu_solve(LU_data, LU_pivots) -> Tensor
        
        See :func:`torch.lu_solve`
        """
        pass

    def map2_(self, *args, **kwargs): # real signature unknown
        pass

    def map_(self, tensor, callable): # real signature unknown; restored from __doc__
        """
        map_(tensor, callable)
        
        Applies :attr:`callable` for each element in :attr:`self` tensor and the given
        :attr:`tensor` and stores the results in :attr:`self` tensor. :attr:`self` tensor and
        the given :attr:`tensor` must be :ref:`broadcastable <broadcasting-semantics>`.
        
        The :attr:`callable` should have the signature::
        
            def callable(a, b) -> number
        """
        pass

    def masked_fill(self, mask, value): # real signature unknown; restored from __doc__
        """
        masked_fill(mask, value) -> Tensor
        
        Out-of-place version of :meth:`torch.Tensor.masked_fill_`
        """
        pass

    def masked_fill_(self, mask, value): # real signature unknown; restored from __doc__
        """
        masked_fill_(mask, value)
        
        Fills elements of :attr:`self` tensor with :attr:`value` where :attr:`mask` is
        True. The shape of :attr:`mask` must be
        :ref:`broadcastable <broadcasting-semantics>` with the shape of the underlying
        tensor.
        
        Args:
            mask (BoolTensor): the boolean mask
            value (float): the value to fill in with
        """
        pass

    def masked_scatter(self, mask, tensor): # real signature unknown; restored from __doc__
        """
        masked_scatter(mask, tensor) -> Tensor
        
        Out-of-place version of :meth:`torch.Tensor.masked_scatter_`
        """
        pass

    def masked_scatter_(self, mask, source): # real signature unknown; restored from __doc__
        """
        masked_scatter_(mask, source)
        
        Copies elements from :attr:`source` into :attr:`self` tensor at positions where
        the :attr:`mask` is True.
        The shape of :attr:`mask` must be :ref:`broadcastable <broadcasting-semantics>`
        with the shape of the underlying tensor. The :attr:`source` should have at least
        as many elements as the number of ones in :attr:`mask`
        
        Args:
            mask (BoolTensor): the boolean mask
            source (Tensor): the tensor to copy from
        
        .. note::
        
            The :attr:`mask` operates on the :attr:`self` tensor, not on the given
            :attr:`source` tensor.
        """
        pass

    def masked_select(self, mask): # real signature unknown; restored from __doc__
        """
        masked_select(mask) -> Tensor
        
        See :func:`torch.masked_select`
        """
        pass

    def matmul(self, tensor2): # real signature unknown; restored from __doc__
        """
        matmul(tensor2) -> Tensor
        
        See :func:`torch.matmul`
        """
        pass

    def matrix_power(self, n): # real signature unknown; restored from __doc__
        """
        matrix_power(n) -> Tensor
        
        See :func:`torch.matrix_power`
        """
        pass

    def max(self, dim=None, keepdim=False): # real signature unknown; restored from __doc__
        """
        max(dim=None, keepdim=False) -> Tensor or (Tensor, Tensor)
        
        See :func:`torch.max`
        """
        pass

    def mean(self, dim=None, keepdim=False): # real signature unknown; restored from __doc__
        """
        mean(dim=None, keepdim=False) -> Tensor or (Tensor, Tensor)
        
        See :func:`torch.mean`
        """
        pass

    def median(self, dim=None, keepdim=False): # real signature unknown; restored from __doc__
        """
        median(dim=None, keepdim=False) -> (Tensor, LongTensor)
        
        See :func:`torch.median`
        """
        pass

    def min(self, dim=None, keepdim=False): # real signature unknown; restored from __doc__
        """
        min(dim=None, keepdim=False) -> Tensor or (Tensor, Tensor)
        
        See :func:`torch.min`
        """
        pass

    def mm(self, mat2): # real signature unknown; restored from __doc__
        """
        mm(mat2) -> Tensor
        
        See :func:`torch.mm`
        """
        pass

    def mode(self, dim=None, keepdim=False): # real signature unknown; restored from __doc__
        """
        mode(dim=None, keepdim=False) -> (Tensor, LongTensor)
        
        See :func:`torch.mode`
        """
        pass

    def mul(self, value): # real signature unknown; restored from __doc__
        """
        mul(value) -> Tensor
        
        See :func:`torch.mul`
        """
        pass

    def multinomial(self, num_samples, replacement=False, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        multinomial(num_samples, replacement=False, *, generator=None) -> Tensor
        
        See :func:`torch.multinomial`
        """
        pass

    def mul_(self, value): # real signature unknown; restored from __doc__
        """
        mul_(value)
        
        In-place version of :meth:`~Tensor.mul`
        """
        pass

    def mv(self, vec): # real signature unknown; restored from __doc__
        """
        mv(vec) -> Tensor
        
        See :func:`torch.mv`
        """
        pass

    def mvlgamma(self, p): # real signature unknown; restored from __doc__
        """
        mvlgamma(p) -> Tensor
        
        See :func:`torch.mvlgamma`
        """
        pass

    def mvlgamma_(self, p): # real signature unknown; restored from __doc__
        """
        mvlgamma_(p) -> Tensor
        
        In-place version of :meth:`~Tensor.mvlgamma`
        """
        pass

    def narrow(self, dimension, start, length): # real signature unknown; restored from __doc__
        """
        narrow(dimension, start, length) -> Tensor
        
        See :func:`torch.narrow`
        
        Example::
        
            >>> x = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
            >>> x.narrow(0, 0, 2)
            tensor([[ 1,  2,  3],
                    [ 4,  5,  6]])
            >>> x.narrow(1, 1, 2)
            tensor([[ 2,  3],
                    [ 5,  6],
                    [ 8,  9]])
        """
        pass

    def narrow_copy(self, dimension, start, length): # real signature unknown; restored from __doc__
        """
        narrow_copy(dimension, start, length) -> Tensor
        
        Same as :meth:`Tensor.narrow` except returning a copy rather
        than shared storage.  This is primarily for sparse tensors, which
        do not have a shared-storage narrow method.  Calling ```narrow_copy``
        with ```dimemsion > self.sparse_dim()``` will return a copy with the
        relevant dense dimension narrowed, and ```self.shape``` updated accordingly.
        """
        pass

    def ndimension(self): # real signature unknown; restored from __doc__
        """
        ndimension() -> int
        
        Alias for :meth:`~Tensor.dim()`
        """
        return 0

    def ne(self, other): # real signature unknown; restored from __doc__
        """
        ne(other) -> Tensor
        
        See :func:`torch.ne`
        """
        pass

    def neg(self): # real signature unknown; restored from __doc__
        """
        neg() -> Tensor
        
        See :func:`torch.neg`
        """
        pass

    def neg_(self): # real signature unknown; restored from __doc__
        """
        neg_() -> Tensor
        
        In-place version of :meth:`~Tensor.neg`
        """
        pass

    def nelement(self): # real signature unknown; restored from __doc__
        """
        nelement() -> int
        
        Alias for :meth:`~Tensor.numel`
        """
        return 0

    def new(self, *args, **kwargs): # real signature unknown
        pass

    def new_empty(self, size, dtype=None, device=None, requires_grad=False): # real signature unknown; restored from __doc__
        """
        new_empty(size, dtype=None, device=None, requires_grad=False) -> Tensor
        
        Returns a Tensor of size :attr:`size` filled with uninitialized data.
        By default, the returned Tensor has the same :class:`torch.dtype` and
        :class:`torch.device` as this tensor.
        
        Args:
            dtype (:class:`torch.dtype`, optional): the desired type of returned tensor.
                Default: if None, same :class:`torch.dtype` as this tensor.
            device (:class:`torch.device`, optional): the desired device of returned tensor.
                Default: if None, same :class:`torch.device` as this tensor.
            requires_grad (bool, optional): If autograd should record operations on the
                returned tensor. Default: ``False``.
        
        Example::
        
            >>> tensor = torch.ones(())
            >>> tensor.new_empty((2, 3))
            tensor([[ 5.8182e-18,  4.5765e-41, -1.0545e+30],
                    [ 3.0949e-41,  4.4842e-44,  0.0000e+00]])
        """
        pass

    def new_full(self, size, fill_value, dtype=None, device=None, requires_grad=False): # real signature unknown; restored from __doc__
        """
        new_full(size, fill_value, dtype=None, device=None, requires_grad=False) -> Tensor
        
        Returns a Tensor of size :attr:`size` filled with :attr:`fill_value`.
        By default, the returned Tensor has the same :class:`torch.dtype` and
        :class:`torch.device` as this tensor.
        
        Args:
            fill_value (scalar): the number to fill the output tensor with.
            dtype (:class:`torch.dtype`, optional): the desired type of returned tensor.
                Default: if None, same :class:`torch.dtype` as this tensor.
            device (:class:`torch.device`, optional): the desired device of returned tensor.
                Default: if None, same :class:`torch.device` as this tensor.
            requires_grad (bool, optional): If autograd should record operations on the
                returned tensor. Default: ``False``.
        
        Example::
        
            >>> tensor = torch.ones((2,), dtype=torch.float64)
            >>> tensor.new_full((3, 4), 3.141592)
            tensor([[ 3.1416,  3.1416,  3.1416,  3.1416],
                    [ 3.1416,  3.1416,  3.1416,  3.1416],
                    [ 3.1416,  3.1416,  3.1416,  3.1416]], dtype=torch.float64)
        """
        pass

    def new_ones(self, size, dtype=None, device=None, requires_grad=False): # real signature unknown; restored from __doc__
        """
        new_ones(size, dtype=None, device=None, requires_grad=False) -> Tensor
        
        Returns a Tensor of size :attr:`size` filled with ``1``.
        By default, the returned Tensor has the same :class:`torch.dtype` and
        :class:`torch.device` as this tensor.
        
        Args:
            size (int...): a list, tuple, or :class:`torch.Size` of integers defining the
                shape of the output tensor.
            dtype (:class:`torch.dtype`, optional): the desired type of returned tensor.
                Default: if None, same :class:`torch.dtype` as this tensor.
            device (:class:`torch.device`, optional): the desired device of returned tensor.
                Default: if None, same :class:`torch.device` as this tensor.
            requires_grad (bool, optional): If autograd should record operations on the
                returned tensor. Default: ``False``.
        
        Example::
        
            >>> tensor = torch.tensor((), dtype=torch.int32)
            >>> tensor.new_ones((2, 3))
            tensor([[ 1,  1,  1],
                    [ 1,  1,  1]], dtype=torch.int32)
        """
        pass

    def new_tensor(self, data, dtype=None, device=None, requires_grad=False): # real signature unknown; restored from __doc__
        """
        new_tensor(data, dtype=None, device=None, requires_grad=False) -> Tensor
        
        Returns a new Tensor with :attr:`data` as the tensor data.
        By default, the returned Tensor has the same :class:`torch.dtype` and
        :class:`torch.device` as this tensor.
        
        .. warning::
        
            :func:`new_tensor` always copies :attr:`data`. If you have a Tensor
            ``data`` and want to avoid a copy, use :func:`torch.Tensor.requires_grad_`
            or :func:`torch.Tensor.detach`.
            If you have a numpy array and want to avoid a copy, use
            :func:`torch.from_numpy`.
        
        .. warning::
        
            When data is a tensor `x`, :func:`new_tensor()` reads out 'the data' from whatever it is passed,
            and constructs a leaf variable. Therefore ``tensor.new_tensor(x)`` is equivalent to ``x.clone().detach()``
            and ``tensor.new_tensor(x, requires_grad=True)`` is equivalent to ``x.clone().detach().requires_grad_(True)``.
            The equivalents using ``clone()`` and ``detach()`` are recommended.
        
        Args:
            data (array_like): The returned Tensor copies :attr:`data`.
            dtype (:class:`torch.dtype`, optional): the desired type of returned tensor.
                Default: if None, same :class:`torch.dtype` as this tensor.
            device (:class:`torch.device`, optional): the desired device of returned tensor.
                Default: if None, same :class:`torch.device` as this tensor.
            requires_grad (bool, optional): If autograd should record operations on the
                returned tensor. Default: ``False``.
        
        Example::
        
            >>> tensor = torch.ones((2,), dtype=torch.int8)
            >>> data = [[0, 1], [2, 3]]
            >>> tensor.new_tensor(data)
            tensor([[ 0,  1],
                    [ 2,  3]], dtype=torch.int8)
        """
        pass

    def new_zeros(self, size, dtype=None, device=None, requires_grad=False): # real signature unknown; restored from __doc__
        """
        new_zeros(size, dtype=None, device=None, requires_grad=False) -> Tensor
        
        Returns a Tensor of size :attr:`size` filled with ``0``.
        By default, the returned Tensor has the same :class:`torch.dtype` and
        :class:`torch.device` as this tensor.
        
        Args:
            size (int...): a list, tuple, or :class:`torch.Size` of integers defining the
                shape of the output tensor.
            dtype (:class:`torch.dtype`, optional): the desired type of returned tensor.
                Default: if None, same :class:`torch.dtype` as this tensor.
            device (:class:`torch.device`, optional): the desired device of returned tensor.
                Default: if None, same :class:`torch.device` as this tensor.
            requires_grad (bool, optional): If autograd should record operations on the
                returned tensor. Default: ``False``.
        
        Example::
        
            >>> tensor = torch.tensor((), dtype=torch.float64)
            >>> tensor.new_zeros((2, 3))
            tensor([[ 0.,  0.,  0.],
                    [ 0.,  0.,  0.]], dtype=torch.float64)
        """
        pass

    def ne_(self, other): # real signature unknown; restored from __doc__
        """
        ne_(other) -> Tensor
        
        In-place version of :meth:`~Tensor.ne`
        """
        pass

    def nonzero(self): # real signature unknown; restored from __doc__
        """
        nonzero() -> LongTensor
        
        See :func:`torch.nonzero`
        """
        pass

    def norm(self, p=2, dim=None, keepdim=False): # real signature unknown; restored from __doc__
        """
        norm(p=2, dim=None, keepdim=False) -> Tensor
        
        See :func:`torch.norm`
        """
        pass

    def normal_(self, mean=0, std=1, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        normal_(mean=0, std=1, *, generator=None) -> Tensor
        
        Fills :attr:`self` tensor with elements samples from the normal distribution
        parameterized by :attr:`mean` and :attr:`std`.
        """
        pass

    def numel(self): # real signature unknown; restored from __doc__
        """
        numel() -> int
        
        See :func:`torch.numel`
        """
        return 0

    def numpy(self): # real signature unknown; restored from __doc__
        """
        numpy() -> numpy.ndarray
        
        Returns :attr:`self` tensor as a NumPy :class:`ndarray`. This tensor and the
        returned :class:`ndarray` share the same underlying storage. Changes to
        :attr:`self` tensor will be reflected in the :class:`ndarray` and vice versa.
        """
        pass

    def orgqr(self, input2): # real signature unknown; restored from __doc__
        """
        orgqr(input2) -> Tensor
        
        See :func:`torch.orgqr`
        """
        pass

    def ormqr(self, input2, input3, left=True, transpose=False): # real signature unknown; restored from __doc__
        """
        ormqr(input2, input3, left=True, transpose=False) -> Tensor
        
        See :func:`torch.ormqr`
        """
        pass

    def permute(self, *dims): # real signature unknown; restored from __doc__
        """
        permute(*dims) -> Tensor
        
        Permute the dimensions of this tensor.
        
        Args:
            *dims (int...): The desired ordering of dimensions
        
        Example:
            >>> x = torch.randn(2, 3, 5)
            >>> x.size()
            torch.Size([2, 3, 5])
            >>> x.permute(2, 0, 1).size()
            torch.Size([5, 2, 3])
        """
        pass

    def pinverse(self): # real signature unknown; restored from __doc__
        """
        pinverse() -> Tensor
        
        See :func:`torch.pinverse`
        """
        pass

    def pin_memory(self): # real signature unknown; restored from __doc__
        """
        pin_memory() -> Tensor
        
        Copies the tensor to pinned memory, if it's not already pinned.
        """
        pass

    def polygamma(self, n): # real signature unknown; restored from __doc__
        """
        polygamma(n) -> Tensor
        
        See :func:`torch.polygamma`
        """
        pass

    def polygamma_(self, n): # real signature unknown; restored from __doc__
        """
        polygamma_(n) -> Tensor
        
        In-place version of :meth:`~Tensor.polygamma`
        """
        pass

    def pow(self, exponent): # real signature unknown; restored from __doc__
        """
        pow(exponent) -> Tensor
        
        See :func:`torch.pow`
        """
        pass

    def pow_(self, exponent): # real signature unknown; restored from __doc__
        """
        pow_(exponent) -> Tensor
        
        In-place version of :meth:`~Tensor.pow`
        """
        pass

    def prelu(self, *args, **kwargs): # real signature unknown
        pass

    def prod(self, dim=None, keepdim=False, dtype=None): # real signature unknown; restored from __doc__
        """
        prod(dim=None, keepdim=False, dtype=None) -> Tensor
        
        See :func:`torch.prod`
        """
        pass

    def put_(self, indices, tensor, accumulate=False): # real signature unknown; restored from __doc__
        """
        put_(indices, tensor, accumulate=False) -> Tensor
        
        Copies the elements from :attr:`tensor` into the positions specified by
        indices. For the purpose of indexing, the :attr:`self` tensor is treated as if
        it were a 1-D tensor.
        
        If :attr:`accumulate` is ``True``, the elements in :attr:`tensor` are added to
        :attr:`self`. If accumulate is ``False``, the behavior is undefined if indices
        contain duplicate elements.
        
        Args:
            indices (LongTensor): the indices into self
            tensor (Tensor): the tensor containing values to copy from
            accumulate (bool): whether to accumulate into self
        
        Example::
        
            >>> src = torch.tensor([[4, 3, 5],
                                    [6, 7, 8]])
            >>> src.put_(torch.tensor([1, 3]), torch.tensor([9, 10]))
            tensor([[  4,   9,   5],
                    [ 10,   7,   8]])
        """
        pass

    def qr(self, some=True): # real signature unknown; restored from __doc__
        """
        qr(some=True) -> (Tensor, Tensor)
        
        See :func:`torch.qr`
        """
        pass

    def qscheme(self): # real signature unknown; restored from __doc__
        """
        qscheme() -> torch.qscheme
        
        Returns the quantization scheme of a given QTensor.
        """
        pass

    def q_per_channel_axis(self): # real signature unknown; restored from __doc__
        """
        q_per_channel_axis() -> int
        
        Given a Tensor quantized by linear (affine) per-channel quantization,
        returns the index of dimension on which per-channel quantization is applied.
        """
        return 0

    def q_per_channel_scales(self): # real signature unknown; restored from __doc__
        """
        q_per_channel_scales() -> Tensor
        
        Given a Tensor quantized by linear (affine) per-channel quantization,
        returns a Tensor of scales of the underlying quantizer. It has the number of
        elements that matches the corresponding dimensions (from q_per_channel_axis) of
        the tensor.
        """
        pass

    def q_per_channel_zero_points(self): # real signature unknown; restored from __doc__
        """
        q_per_channel_zero_points() -> Tensor
        
        Given a Tensor quantized by linear (affine) per-channel quantization,
        returns a tensor of zero_points of the underlying quantizer. It has the number of
        elements that matches the corresponding dimensions (from q_per_channel_axis) of
        the tensor.
        """
        pass

    def q_scale(self): # real signature unknown; restored from __doc__
        """
        q_scale() -> float
        
        Given a Tensor quantized by linear(affine) quantization,
        returns the scale of the underlying quantizer().
        """
        return 0.0

    def q_zero_point(self): # real signature unknown; restored from __doc__
        """
        q_zero_point() -> int
        
        Given a Tensor quantized by linear(affine) quantization,
        returns the zero_point of the underlying quantizer().
        """
        return 0

    def random_(self, from=0, to=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        random_(from=0, to=None, *, generator=None) -> Tensor
        
        Fills :attr:`self` tensor with numbers sampled from the discrete uniform
        distribution over ``[from, to - 1]``. If not specified, the values are usually
        only bounded by :attr:`self` tensor's data type. However, for floating point
        types, if unspecified, range will be ``[0, 2^mantissa]`` to ensure that every
        value is representable. For example, `torch.tensor(1, dtype=torch.double).random_()`
        will be uniform in ``[0, 2^53]``.
        """
        pass

    def reciprocal(self): # real signature unknown; restored from __doc__
        """
        reciprocal() -> Tensor
        
        See :func:`torch.reciprocal`
        """
        pass

    def reciprocal_(self): # real signature unknown; restored from __doc__
        """
        reciprocal_() -> Tensor
        
        In-place version of :meth:`~Tensor.reciprocal`
        """
        pass

    def record_stream(self, stream): # real signature unknown; restored from __doc__
        """
        record_stream(stream)
        
        Ensures that the tensor memory is not reused for another tensor until all
        current work queued on :attr:`stream` are complete.
        
        .. note::
        
            The caching allocator is aware of only the stream where a tensor was
            allocated. Due to the awareness, it already correctly manages the life
            cycle of tensors on only one stream. But if a tensor is used on a stream
            different from the stream of origin, the allocator might reuse the memory
            unexpectedly. Calling this method lets the allocator know which streams
            have used the tensor.
        """
        pass

    def refine_names(self, *args, **kwargs): # real signature unknown
        pass

    def relu(self, *args, **kwargs): # real signature unknown
        pass

    def relu_(self, *args, **kwargs): # real signature unknown
        pass

    def remainder(self, divisor): # real signature unknown; restored from __doc__
        """
        remainder(divisor) -> Tensor
        
        See :func:`torch.remainder`
        """
        pass

    def remainder_(self, divisor): # real signature unknown; restored from __doc__
        """
        remainder_(divisor) -> Tensor
        
        In-place version of :meth:`~Tensor.remainder`
        """
        pass

    def rename(self, *args, **kwargs): # real signature unknown
        pass

    def rename_(self, *args, **kwargs): # real signature unknown
        pass

    def renorm(self, p, dim, maxnorm): # real signature unknown; restored from __doc__
        """
        renorm(p, dim, maxnorm) -> Tensor
        
        See :func:`torch.renorm`
        """
        pass

    def renorm_(self, p, dim, maxnorm): # real signature unknown; restored from __doc__
        """
        renorm_(p, dim, maxnorm) -> Tensor
        
        In-place version of :meth:`~Tensor.renorm`
        """
        pass

    def repeat(self, *sizes): # real signature unknown; restored from __doc__
        """
        repeat(*sizes) -> Tensor
        
        Repeats this tensor along the specified dimensions.
        
        Unlike :meth:`~Tensor.expand`, this function copies the tensor's data.
        
        .. warning::
        
            :func:`torch.repeat` behaves differently from
            `numpy.repeat <https://docs.scipy.org/doc/numpy/reference/generated/numpy.repeat.html>`_,
            but is more similar to
            `numpy.tile <https://docs.scipy.org/doc/numpy/reference/generated/numpy.tile.html>`_.
            For the operator similar to `numpy.repeat`, see :func:`torch.repeat_interleave`.
        
        Args:
            sizes (torch.Size or int...): The number of times to repeat this tensor along each
                dimension
        
        Example::
        
            >>> x = torch.tensor([1, 2, 3])
            >>> x.repeat(4, 2)
            tensor([[ 1,  2,  3,  1,  2,  3],
                    [ 1,  2,  3,  1,  2,  3],
                    [ 1,  2,  3,  1,  2,  3],
                    [ 1,  2,  3,  1,  2,  3]])
            >>> x.repeat(4, 2, 1).size()
            torch.Size([4, 2, 3])
        """
        pass

    def repeat_interleave(self, repeats, dim=None): # real signature unknown; restored from __doc__
        """
        repeat_interleave(repeats, dim=None) -> Tensor
        
        See :func:`torch.repeat_interleave`.
        """
        pass

    def requires_grad_(self, requires_grad=True): # real signature unknown; restored from __doc__
        """
        requires_grad_(requires_grad=True) -> Tensor
        
        Change if autograd should record operations on this tensor: sets this tensor's
        :attr:`requires_grad` attribute in-place. Returns this tensor.
        
        :func:`requires_grad_`'s main use case is to tell autograd to begin recording
        operations on a Tensor ``tensor``. If ``tensor`` has ``requires_grad=False``
        (because it was obtained through a DataLoader, or required preprocessing or
        initialization), ``tensor.requires_grad_()`` makes it so that autograd will
        begin to record operations on ``tensor``.
        
        Args:
            requires_grad (bool): If autograd should record operations on this tensor.
                Default: ``True``.
        
        Example::
        
            >>> # Let's say we want to preprocess some saved weights and use
            >>> # the result as new weights.
            >>> saved_weights = [0.1, 0.2, 0.3, 0.25]
            >>> loaded_weights = torch.tensor(saved_weights)
            >>> weights = preprocess(loaded_weights)  # some function
            >>> weights
            tensor([-0.5503,  0.4926, -2.1158, -0.8303])
        
            >>> # Now, start to record operations done to weights
            >>> weights.requires_grad_()
            >>> out = weights.pow(2).sum()
            >>> out.backward()
            >>> weights.grad
            tensor([-1.1007,  0.9853, -4.2316, -1.6606])
        """
        pass

    def reshape(self, *shape): # real signature unknown; restored from __doc__
        """
        reshape(*shape) -> Tensor
        
        Returns a tensor with the same data and number of elements as :attr:`self`
        but with the specified shape. This method returns a view if :attr:`shape` is
        compatible with the current shape. See :meth:`torch.Tensor.view` on when it is
        possible to return a view.
        
        See :func:`torch.reshape`
        
        Args:
            shape (tuple of ints or int...): the desired shape
        """
        pass

    def reshape_as(self, other): # real signature unknown; restored from __doc__
        """
        reshape_as(other) -> Tensor
        
        Returns this tensor as the same shape as :attr:`other`.
        ``self.reshape_as(other)`` is equivalent to ``self.reshape(other.sizes())``.
        This method returns a view if ``other.sizes()`` is compatible with the current
        shape. See :meth:`torch.Tensor.view` on when it is possible to return a view.
        
        Please see :meth:`reshape` for more information about ``reshape``.
        
        Args:
            other (:class:`torch.Tensor`): The result tensor has the same shape
                as :attr:`other`.
        """
        pass

    def resize_(self, *sizes): # real signature unknown; restored from __doc__
        """
        resize_(*sizes) -> Tensor
        
        Resizes :attr:`self` tensor to the specified size. If the number of elements is
        larger than the current storage size, then the underlying storage is resized
        to fit the new number of elements. If the number of elements is smaller, the
        underlying storage is not changed. Existing elements are preserved but any new
        memory is uninitialized.
        
        .. warning::
        
            This is a low-level method. The storage is reinterpreted as C-contiguous,
            ignoring the current strides (unless the target size equals the current
            size, in which case the tensor is left unchanged). For most purposes, you
            will instead want to use :meth:`~Tensor.view()`, which checks for
            contiguity, or :meth:`~Tensor.reshape()`, which copies data if needed. To
            change the size in-place with custom strides, see :meth:`~Tensor.set_()`.
        
        Args:
            sizes (torch.Size or int...): the desired size
        
        Example::
        
            >>> x = torch.tensor([[1, 2], [3, 4], [5, 6]])
            >>> x.resize_(2, 2)
            tensor([[ 1,  2],
                    [ 3,  4]])
        """
        pass

    def resize_as_(self, tensor): # real signature unknown; restored from __doc__
        """
        resize_as_(tensor) -> Tensor
        
        Resizes the :attr:`self` tensor to be the same size as the specified
        :attr:`tensor`. This is equivalent to ``self.resize_(tensor.size())``.
        """
        pass

    def rfft(self, signal_ndim, normalized=False, onesided=True): # real signature unknown; restored from __doc__
        """
        rfft(signal_ndim, normalized=False, onesided=True) -> Tensor
        
        See :func:`torch.rfft`
        """
        pass

    def roll(self, shifts, dims): # real signature unknown; restored from __doc__
        """
        roll(shifts, dims) -> Tensor
        
        See :func:`torch.roll`
        """
        pass

    def rot90(self, k, dims): # real signature unknown; restored from __doc__
        """
        rot90(k, dims) -> Tensor
        
        See :func:`torch.rot90`
        """
        pass

    def round(self): # real signature unknown; restored from __doc__
        """
        round() -> Tensor
        
        See :func:`torch.round`
        """
        pass

    def round_(self): # real signature unknown; restored from __doc__
        """
        round_() -> Tensor
        
        In-place version of :meth:`~Tensor.round`
        """
        pass

    def rsqrt(self): # real signature unknown; restored from __doc__
        """
        rsqrt() -> Tensor
        
        See :func:`torch.rsqrt`
        """
        pass

    def rsqrt_(self): # real signature unknown; restored from __doc__
        """
        rsqrt_() -> Tensor
        
        In-place version of :meth:`~Tensor.rsqrt`
        """
        pass

    def scatter(self, dim, index, source): # real signature unknown; restored from __doc__
        """
        scatter(dim, index, source) -> Tensor
        
        Out-of-place version of :meth:`torch.Tensor.scatter_`
        """
        pass

    def scatter_(self, dim, index, src): # real signature unknown; restored from __doc__
        """
        scatter_(dim, index, src) -> Tensor
        
        Writes all values from the tensor :attr:`src` into :attr:`self` at the indices
        specified in the :attr:`index` tensor. For each value in :attr:`src`, its output
        index is specified by its index in :attr:`src` for ``dimension != dim`` and by
        the corresponding value in :attr:`index` for ``dimension = dim``.
        
        For a 3-D tensor, :attr:`self` is updated as::
        
            self[index[i][j][k]][j][k] = src[i][j][k]  # if dim == 0
            self[i][index[i][j][k]][k] = src[i][j][k]  # if dim == 1
            self[i][j][index[i][j][k]] = src[i][j][k]  # if dim == 2
        
        This is the reverse operation of the manner described in :meth:`~Tensor.gather`.
        
        :attr:`self`, :attr:`index` and :attr:`src` (if it is a Tensor) should have same
        number of dimensions. It is also required that ``index.size(d) <= src.size(d)``
        for all dimensions ``d``, and that ``index.size(d) <= self.size(d)`` for all
        dimensions ``d != dim``.
        
        Moreover, as for :meth:`~Tensor.gather`, the values of :attr:`index` must be
        between ``0`` and ``self.size(dim) - 1`` inclusive, and all values in a row
        along the specified dimension :attr:`dim` must be unique.
        
        Args:
            dim (int): the axis along which to index
            index (LongTensor): the indices of elements to scatter,
              can be either empty or the same size of src.
              When empty, the operation returns identity
            src (Tensor): the source element(s) to scatter,
              incase `value` is not specified
            value (float): the source element(s) to scatter,
              incase `src` is not specified
        
        Example::
        
            >>> x = torch.rand(2, 5)
            >>> x
            tensor([[ 0.3992,  0.2908,  0.9044,  0.4850,  0.6004],
                    [ 0.5735,  0.9006,  0.6797,  0.4152,  0.1732]])
            >>> torch.zeros(3, 5).scatter_(0, torch.tensor([[0, 1, 2, 0, 0], [2, 0, 0, 1, 2]]), x)
            tensor([[ 0.3992,  0.9006,  0.6797,  0.4850,  0.6004],
                    [ 0.0000,  0.2908,  0.0000,  0.4152,  0.0000],
                    [ 0.5735,  0.0000,  0.9044,  0.0000,  0.1732]])
        
            >>> z = torch.zeros(2, 4).scatter_(1, torch.tensor([[2], [3]]), 1.23)
            >>> z
            tensor([[ 0.0000,  0.0000,  1.2300,  0.0000],
                    [ 0.0000,  0.0000,  0.0000,  1.2300]])
        """
        pass

    def scatter_add(self, dim, index, source): # real signature unknown; restored from __doc__
        """
        scatter_add(dim, index, source) -> Tensor
        
        Out-of-place version of :meth:`torch.Tensor.scatter_add_`
        """
        pass

    def scatter_add_(self, dim, index, other): # real signature unknown; restored from __doc__
        """
        scatter_add_(dim, index, other) -> Tensor
        
        Adds all values from the tensor :attr:`other` into :attr:`self` at the indices
        specified in the :attr:`index` tensor in a similar fashion as
        :meth:`~torch.Tensor.scatter_`. For each value in :attr:`other`, it is added to
        an index in :attr:`self` which is specified by its index in :attr:`other`
        for ``dimension != dim`` and by the corresponding value in :attr:`index` for
        ``dimension = dim``.
        
        For a 3-D tensor, :attr:`self` is updated as::
        
            self[index[i][j][k]][j][k] += other[i][j][k]  # if dim == 0
            self[i][index[i][j][k]][k] += other[i][j][k]  # if dim == 1
            self[i][j][index[i][j][k]] += other[i][j][k]  # if dim == 2
        
        :attr:`self`, :attr:`index` and :attr:`other` should have same number of
        dimensions. It is also required that ``index.size(d) <= other.size(d)`` for all
        dimensions ``d``, and that ``index.size(d) <= self.size(d)`` for all dimensions
        ``d != dim``.
        
        Moreover, as for :meth:`~Tensor.gather`, the values of :attr:`index` must be
        between ``0`` and ``self.size(dim) - 1`` inclusive, and all values in a row along
        the specified dimension :attr:`dim` must be unique.
        
        .. include:: cuda_deterministic.rst
        
        Args:
            dim (int): the axis along which to index
            index (LongTensor): the indices of elements to scatter and add,
              can be either empty or the same size of src.
              When empty, the operation returns identity.
            other (Tensor): the source elements to scatter and add
        
        Example::
        
            >>> x = torch.rand(2, 5)
            >>> x
            tensor([[0.7404, 0.0427, 0.6480, 0.3806, 0.8328],
                    [0.7953, 0.2009, 0.9154, 0.6782, 0.9620]])
            >>> torch.ones(3, 5).scatter_add_(0, torch.tensor([[0, 1, 2, 0, 0], [2, 0, 0, 1, 2]]), x)
            tensor([[1.7404, 1.2009, 1.9154, 1.3806, 1.8328],
                    [1.0000, 1.0427, 1.0000, 1.6782, 1.0000],
                    [1.7953, 1.0000, 1.6480, 1.0000, 1.9620]])
        """
        pass

    def select(self, dim, index): # real signature unknown; restored from __doc__
        """
        select(dim, index) -> Tensor
        
        Slices the :attr:`self` tensor along the selected dimension at the given index.
        This function returns a tensor with the given dimension removed.
        
        Args:
            dim (int): the dimension to slice
            index (int): the index to select with
        
        .. note::
        
            :meth:`select` is equivalent to slicing. For example,
            ``tensor.select(0, index)`` is equivalent to ``tensor[index]`` and
            ``tensor.select(2, index)`` is equivalent to ``tensor[:,:,index]``.
        """
        pass

    def set_(self, source=None, storage_offset=0, size=None, stride=None): # real signature unknown; restored from __doc__
        """
        set_(source=None, storage_offset=0, size=None, stride=None) -> Tensor
        
        Sets the underlying storage, size, and strides. If :attr:`source` is a tensor,
        :attr:`self` tensor will share the same storage and have the same size and
        strides as :attr:`source`. Changes to elements in one tensor will be reflected
        in the other.
        
        If :attr:`source` is a :class:`~torch.Storage`, the method sets the underlying
        storage, offset, size, and stride.
        
        Args:
            source (Tensor or Storage): the tensor or storage to use
            storage_offset (int, optional): the offset in the storage
            size (torch.Size, optional): the desired size. Defaults to the size of the source.
            stride (tuple, optional): the desired stride. Defaults to C-contiguous strides.
        """
        pass

    def short(self): # real signature unknown; restored from __doc__
        """
        short() -> Tensor
        
        ``self.short()`` is equivalent to ``self.to(torch.int16)``. See :func:`to`.
        """
        pass

    def sigmoid(self): # real signature unknown; restored from __doc__
        """
        sigmoid() -> Tensor
        
        See :func:`torch.sigmoid`
        """
        pass

    def sigmoid_(self): # real signature unknown; restored from __doc__
        """
        sigmoid_() -> Tensor
        
        In-place version of :meth:`~Tensor.sigmoid`
        """
        pass

    def sign(self): # real signature unknown; restored from __doc__
        """
        sign() -> Tensor
        
        See :func:`torch.sign`
        """
        pass

    def sign_(self): # real signature unknown; restored from __doc__
        """
        sign_() -> Tensor
        
        In-place version of :meth:`~Tensor.sign`
        """
        pass

    def sin(self): # real signature unknown; restored from __doc__
        """
        sin() -> Tensor
        
        See :func:`torch.sin`
        """
        pass

    def sinh(self): # real signature unknown; restored from __doc__
        """
        sinh() -> Tensor
        
        See :func:`torch.sinh`
        """
        pass

    def sinh_(self): # real signature unknown; restored from __doc__
        """
        sinh_() -> Tensor
        
        In-place version of :meth:`~Tensor.sinh`
        """
        pass

    def sin_(self): # real signature unknown; restored from __doc__
        """
        sin_() -> Tensor
        
        In-place version of :meth:`~Tensor.sin`
        """
        pass

    def size(self): # real signature unknown; restored from __doc__
        """
        size() -> torch.Size
        
        Returns the size of the :attr:`self` tensor. The returned value is a subclass of
        :class:`tuple`.
        
        Example::
        
            >>> torch.empty(3, 4, 5).size()
            torch.Size([3, 4, 5])
        """
        pass

    def slogdet(self): # real signature unknown; restored from __doc__
        """
        slogdet() -> (Tensor, Tensor)
        
        See :func:`torch.slogdet`
        """
        pass

    def smm(self, *args, **kwargs): # real signature unknown
        pass

    def softmax(self, *args, **kwargs): # real signature unknown
        pass

    def solve(self, A): # real signature unknown; restored from __doc__
        """
        solve(A) -> Tensor, Tensor
        
        See :func:`torch.solve`
        """
        pass

    def sort(self, dim=-1, descending=False): # real signature unknown; restored from __doc__
        """
        sort(dim=-1, descending=False) -> (Tensor, LongTensor)
        
        See :func:`torch.sort`
        """
        pass

    def sparse_dim(self): # real signature unknown; restored from __doc__
        """
        sparse_dim() -> int
        
        If :attr:`self` is a sparse COO tensor (i.e., with ``torch.sparse_coo`` layout),
        this returns the number of sparse dimensions. Otherwise, this throws an error.
        
        See also :meth:`Tensor.dense_dim`.
        """
        return 0

    def sparse_mask(self, input, mask): # real signature unknown; restored from __doc__
        """
        sparse_mask(input, mask) -> Tensor
        
        Returns a new SparseTensor with values from Tensor :attr:`input` filtered
        by indices of :attr:`mask` and values are ignored. :attr:`input` and :attr:`mask`
        must have the same shape.
        
        Args:
            input (Tensor): an input Tensor
            mask (SparseTensor): a SparseTensor which we filter :attr:`input` based on its indices
        
        Example::
        
            >>> nnz = 5
            >>> dims = [5, 5, 2, 2]
            >>> I = torch.cat([torch.randint(0, dims[0], size=(nnz,)),
                               torch.randint(0, dims[1], size=(nnz,))], 0).reshape(2, nnz)
            >>> V = torch.randn(nnz, dims[2], dims[3])
            >>> size = torch.Size(dims)
            >>> S = torch.sparse_coo_tensor(I, V, size).coalesce()
            >>> D = torch.randn(dims)
            >>> D.sparse_mask(S)
            tensor(indices=tensor([[0, 0, 0, 2],
                                   [0, 1, 4, 3]]),
                   values=tensor([[[ 1.6550,  0.2397],
                                   [-0.1611, -0.0779]],
        
                                  [[ 0.2326, -1.0558],
                                   [ 1.4711,  1.9678]],
        
                                  [[-0.5138, -0.0411],
                                   [ 1.9417,  0.5158]],
        
                                  [[ 0.0793,  0.0036],
                                   [-0.2569, -0.1055]]]),
                   size=(5, 5, 2, 2), nnz=4, layout=torch.sparse_coo)
        """
        pass

    def sparse_resize_(self, *args, **kwargs): # real signature unknown
        pass

    def sparse_resize_and_clear_(self, *args, **kwargs): # real signature unknown
        pass

    def split(self, *args, **kwargs): # real signature unknown
        pass

    def split_with_sizes(self, *args, **kwargs): # real signature unknown
        pass

    def sqrt(self): # real signature unknown; restored from __doc__
        """
        sqrt() -> Tensor
        
        See :func:`torch.sqrt`
        """
        pass

    def sqrt_(self): # real signature unknown; restored from __doc__
        """
        sqrt_() -> Tensor
        
        In-place version of :meth:`~Tensor.sqrt`
        """
        pass

    def squeeze(self, dim=None): # real signature unknown; restored from __doc__
        """
        squeeze(dim=None) -> Tensor
        
        See :func:`torch.squeeze`
        """
        pass

    def squeeze_(self, dim=None): # real signature unknown; restored from __doc__
        """
        squeeze_(dim=None) -> Tensor
        
        In-place version of :meth:`~Tensor.squeeze`
        """
        pass

    def sspaddmm(self, *args, **kwargs): # real signature unknown
        pass

    def std(self, dim=None, unbiased=True, keepdim=False): # real signature unknown; restored from __doc__
        """
        std(dim=None, unbiased=True, keepdim=False) -> Tensor
        
        See :func:`torch.std`
        """
        pass

    def stft(self, frame_length, hop, fft_size=None, return_onesided=True, window=None, pad_end=0): # real signature unknown; restored from __doc__
        """
        stft(frame_length, hop, fft_size=None, return_onesided=True, window=None, pad_end=0) -> Tensor
        
        See :func:`torch.stft`
        """
        pass

    def storage(self): # real signature unknown; restored from __doc__
        """
        storage() -> torch.Storage
        
        Returns the underlying storage.
        """
        pass

    def storage_offset(self): # real signature unknown; restored from __doc__
        """
        storage_offset() -> int
        
        Returns :attr:`self` tensor's offset in the underlying storage in terms of
        number of storage elements (not bytes).
        
        Example::
        
            >>> x = torch.tensor([1, 2, 3, 4, 5])
            >>> x.storage_offset()
            0
            >>> x[3:].storage_offset()
            3
        """
        return 0

    def storage_type(self): # real signature unknown; restored from __doc__
        """
        storage_type() -> type
        
        Returns the type of the underlying storage.
        """
        return type(*(), **{})

    def stride(self, dim): # real signature unknown; restored from __doc__
        """
        stride(dim) -> tuple or int
        
        Returns the stride of :attr:`self` tensor.
        
        Stride is the jump necessary to go from one element to the next one in the
        specified dimension :attr:`dim`. A tuple of all strides is returned when no
        argument is passed in. Otherwise, an integer value is returned as the stride in
        the particular dimension :attr:`dim`.
        
        Args:
            dim (int, optional): the desired dimension in which stride is required
        
        Example::
        
            >>> x = torch.tensor([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
            >>> x.stride()
            (5, 1)
            >>>x.stride(0)
            5
            >>> x.stride(-1)
            1
        """
        return ()

    def sub(self, value, other): # real signature unknown; restored from __doc__
        """
        sub(value, other) -> Tensor
        
        Subtracts a scalar or tensor from :attr:`self` tensor. If both :attr:`value` and
        :attr:`other` are specified, each element of :attr:`other` is scaled by
        :attr:`value` before being used.
        
        When :attr:`other` is a tensor, the shape of :attr:`other` must be
        :ref:`broadcastable <broadcasting-semantics>` with the shape of the underlying
        tensor.
        """
        pass

    def sub_(self, x): # real signature unknown; restored from __doc__
        """
        sub_(x) -> Tensor
        
        In-place version of :meth:`~Tensor.sub`
        """
        pass

    def sum(self, dim=None, keepdim=False, dtype=None): # real signature unknown; restored from __doc__
        """
        sum(dim=None, keepdim=False, dtype=None) -> Tensor
        
        See :func:`torch.sum`
        """
        pass

    def sum_to_size(self, *size): # real signature unknown; restored from __doc__
        """
        sum_to_size(*size) -> Tensor
        
        Sum ``this`` tensor to :attr:`size`.
        :attr:`size` must be broadcastable to ``this`` tensor size.
        
        Args:
            size (int...): a sequence of integers defining the shape of the output tensor.
        """
        pass

    def svd(self, some=True, compute_uv=True): # real signature unknown; restored from __doc__
        """
        svd(some=True, compute_uv=True) -> (Tensor, Tensor, Tensor)
        
        See :func:`torch.svd`
        """
        pass

    def symeig(self, eigenvectors=False, upper=True): # real signature unknown; restored from __doc__
        """
        symeig(eigenvectors=False, upper=True) -> (Tensor, Tensor)
        
        See :func:`torch.symeig`
        """
        pass

    def t(self): # real signature unknown; restored from __doc__
        """
        t() -> Tensor
        
        See :func:`torch.t`
        """
        pass

    def take(self, indices): # real signature unknown; restored from __doc__
        """
        take(indices) -> Tensor
        
        See :func:`torch.take`
        """
        pass

    def tan(self): # real signature unknown; restored from __doc__
        """
        tan() -> Tensor
        
        See :func:`torch.tan`
        """
        pass

    def tanh(self): # real signature unknown; restored from __doc__
        """
        tanh() -> Tensor
        
        See :func:`torch.tanh`
        """
        pass

    def tanh_(self): # real signature unknown; restored from __doc__
        """
        tanh_() -> Tensor
        
        In-place version of :meth:`~Tensor.tanh`
        """
        pass

    def tan_(self): # real signature unknown; restored from __doc__
        """
        tan_() -> Tensor
        
        In-place version of :meth:`~Tensor.tan`
        """
        pass

    def to(self, *args, **kwargs): # real signature unknown; restored from __doc__
        """
        to(*args, **kwargs) -> Tensor
        
        Performs Tensor dtype and/or device conversion. A :class:`torch.dtype` and :class:`torch.device` are
        inferred from the arguments of ``self.to(*args, **kwargs)``.
        
        .. note::
        
            If the ``self`` Tensor already
            has the correct :class:`torch.dtype` and :class:`torch.device`, then ``self`` is returned.
            Otherwise, the returned tensor is a copy of ``self`` with the desired
            :class:`torch.dtype` and :class:`torch.device`.
        
        Here are the ways to call ``to``:
        
        .. function:: to(dtype, non_blocking=False, copy=False) -> Tensor
        
            Returns a Tensor with the specified :attr:`dtype`
        
        .. function:: to(device=None, dtype=None, non_blocking=False, copy=False) -> Tensor
        
            Returns a Tensor with the specified :attr:`device` and (optional)
            :attr:`dtype`. If :attr:`dtype` is ``None`` it is inferred to be ``self.dtype``.
            When :attr:`non_blocking`, tries to convert asynchronously with respect to
            the host if possible, e.g., converting a CPU Tensor with pinned memory to a
            CUDA Tensor.
            When :attr:`copy` is set, a new Tensor is created even when the Tensor
            already matches the desired conversion.
        
        .. function:: to(other, non_blocking=False, copy=False) -> Tensor
        
            Returns a Tensor with same :class:`torch.dtype` and :class:`torch.device` as
            the Tensor :attr:`other`. When :attr:`non_blocking`, tries to convert
            asynchronously with respect to the host if possible, e.g., converting a CPU
            Tensor with pinned memory to a CUDA Tensor.
            When :attr:`copy` is set, a new Tensor is created even when the Tensor
            already matches the desired conversion.
        
        Example::
        
            >>> tensor = torch.randn(2, 2)  # Initially dtype=float32, device=cpu
            >>> tensor.to(torch.float64)
            tensor([[-0.5044,  0.0005],
                    [ 0.3310, -0.0584]], dtype=torch.float64)
        
            >>> cuda0 = torch.device('cuda:0')
            >>> tensor.to(cuda0)
            tensor([[-0.5044,  0.0005],
                    [ 0.3310, -0.0584]], device='cuda:0')
        
            >>> tensor.to(cuda0, dtype=torch.float64)
            tensor([[-0.5044,  0.0005],
                    [ 0.3310, -0.0584]], dtype=torch.float64, device='cuda:0')
        
            >>> other = torch.randn((), dtype=torch.float64, device=cuda0)
            >>> tensor.to(other, non_blocking=True)
            tensor([[-0.5044,  0.0005],
                    [ 0.3310, -0.0584]], dtype=torch.float64, device='cuda:0')
        """
        pass

    def tolist(self): # real signature unknown; restored from __doc__
        """
        "
        tolist() -> list or number
        
        Returns the tensor as a (nested) list. For scalars, a standard
        Python number is returned, just like with :meth:`~Tensor.item`.
        Tensors are automatically moved to the CPU first if necessary.
        
        This operation is not differentiable.
        
        Examples::
        
            >>> a = torch.randn(2, 2)
            >>> a.tolist()
            [[0.012766935862600803, 0.5415473580360413],
             [-0.08909505605697632, 0.7729271650314331]]
            >>> a[0,0].tolist()
            0.012766935862600803
        """
        return []

    def topk(self, k, dim=None, largest=True, sorted=True): # real signature unknown; restored from __doc__
        """
        topk(k, dim=None, largest=True, sorted=True) -> (Tensor, LongTensor)
        
        See :func:`torch.topk`
        """
        pass

    def to_dense(self, *args, **kwargs): # real signature unknown
        pass

    def to_mkldnn(self): # real signature unknown; restored from __doc__
        """
        to_mkldnn() -> Tensor
        Returns a copy of the tensor in ``torch.mkldnn`` layout.
        """
        pass

    def to_sparse(self, sparseDims): # real signature unknown; restored from __doc__
        """
        to_sparse(sparseDims) -> Tensor
        Returns a sparse copy of the tensor.  PyTorch supports sparse tensors in
        :ref:`coordinate format <sparse-docs>`.
        
        Args:
            sparseDims (int, optional): the number of sparse dimensions to include in the new sparse tensor
        
        Example::
        
            >>> d = torch.tensor([[0, 0, 0], [9, 0, 10], [0, 0, 0]])
            >>> d
            tensor([[ 0,  0,  0],
                    [ 9,  0, 10],
                    [ 0,  0,  0]])
            >>> d.to_sparse()
            tensor(indices=tensor([[1, 1],
                                   [0, 2]]),
                   values=tensor([ 9, 10]),
                   size=(3, 3), nnz=2, layout=torch.sparse_coo)
            >>> d.to_sparse(1)
            tensor(indices=tensor([[1]]),
                   values=tensor([[ 9,  0, 10]]),
                   size=(3, 3), nnz=1, layout=torch.sparse_coo)
        """
        pass

    def trace(self): # real signature unknown; restored from __doc__
        """
        trace() -> Tensor
        
        See :func:`torch.trace`
        """
        pass

    def transpose(self, dim0, dim1): # real signature unknown; restored from __doc__
        """
        transpose(dim0, dim1) -> Tensor
        
        See :func:`torch.transpose`
        """
        pass

    def transpose_(self, dim0, dim1): # real signature unknown; restored from __doc__
        """
        transpose_(dim0, dim1) -> Tensor
        
        In-place version of :meth:`~Tensor.transpose`
        """
        pass

    def triangular_solve(self, A, upper=True, transpose=False, unitriangular=False): # real signature unknown; restored from __doc__
        """
        triangular_solve(A, upper=True, transpose=False, unitriangular=False) -> (Tensor, Tensor)
        
        See :func:`torch.triangular_solve`
        """
        pass

    def tril(self, k=0): # real signature unknown; restored from __doc__
        """
        tril(k=0) -> Tensor
        
        See :func:`torch.tril`
        """
        pass

    def tril_(self, k=0): # real signature unknown; restored from __doc__
        """
        tril_(k=0) -> Tensor
        
        In-place version of :meth:`~Tensor.tril`
        """
        pass

    def triu(self, k=0): # real signature unknown; restored from __doc__
        """
        triu(k=0) -> Tensor
        
        See :func:`torch.triu`
        """
        pass

    def triu_(self, k=0): # real signature unknown; restored from __doc__
        """
        triu_(k=0) -> Tensor
        
        In-place version of :meth:`~Tensor.triu`
        """
        pass

    def trunc(self): # real signature unknown; restored from __doc__
        """
        trunc() -> Tensor
        
        See :func:`torch.trunc`
        """
        pass

    def trunc_(self): # real signature unknown; restored from __doc__
        """
        trunc_() -> Tensor
        
        In-place version of :meth:`~Tensor.trunc`
        """
        pass

    def type(self, dtype=None, non_blocking=False, **kwargs): # real signature unknown; restored from __doc__
        """
        type(dtype=None, non_blocking=False, **kwargs) -> str or Tensor
        Returns the type if `dtype` is not provided, else casts this object to
        the specified type.
        
        If this is already of the correct type, no copy is performed and the
        original object is returned.
        
        Args:
            dtype (type or string): The desired type
            non_blocking (bool): If ``True``, and the source is in pinned memory
                and destination is on the GPU or vice versa, the copy is performed
                asynchronously with respect to the host. Otherwise, the argument
                has no effect.
            **kwargs: For compatibility, may contain the key ``async`` in place of
                the ``non_blocking`` argument. The ``async`` arg is deprecated.
        """
        return ""

    def type_as(self, tensor): # real signature unknown; restored from __doc__
        """
        type_as(tensor) -> Tensor
        
        Returns this tensor cast to the type of the given tensor.
        
        This is a no-op if the tensor is already of the correct type. This is
        equivalent to ``self.type(tensor.type())``
        
        Args:
            tensor (Tensor): the tensor which has the desired type
        """
        pass

    def t_(self): # real signature unknown; restored from __doc__
        """
        t_() -> Tensor
        
        In-place version of :meth:`~Tensor.t`
        """
        pass

    def unbind(self, dim=0): # real signature unknown; restored from __doc__
        """
        unbind(dim=0) -> seq
        
        See :func:`torch.unbind`
        """
        pass

    def unflatten(self, *args, **kwargs): # real signature unknown
        pass

    def unfold(self, dimension, size, step): # real signature unknown; restored from __doc__
        """
        unfold(dimension, size, step) -> Tensor
        
        Returns a tensor which contains all slices of size :attr:`size` from
        :attr:`self` tensor in the dimension :attr:`dimension`.
        
        Step between two slices is given by :attr:`step`.
        
        If `sizedim` is the size of dimension :attr:`dimension` for :attr:`self`, the size of
        dimension :attr:`dimension` in the returned tensor will be
        `(sizedim - size) / step + 1`.
        
        An additional dimension of size :attr:`size` is appended in the returned tensor.
        
        Args:
            dimension (int): dimension in which unfolding happens
            size (int): the size of each slice that is unfolded
            step (int): the step between each slice
        
        Example::
        
            >>> x = torch.arange(1., 8)
            >>> x
            tensor([ 1.,  2.,  3.,  4.,  5.,  6.,  7.])
            >>> x.unfold(0, 2, 1)
            tensor([[ 1.,  2.],
                    [ 2.,  3.],
                    [ 3.,  4.],
                    [ 4.,  5.],
                    [ 5.,  6.],
                    [ 6.,  7.]])
            >>> x.unfold(0, 2, 2)
            tensor([[ 1.,  2.],
                    [ 3.,  4.],
                    [ 5.,  6.]])
        """
        pass

    def uniform_(self, from=0, to=1): # real signature unknown; restored from __doc__
        """
        uniform_(from=0, to=1) -> Tensor
        
        Fills :attr:`self` tensor with numbers sampled from the continuous uniform
        distribution:
        
        .. math::
            P(x) = \dfrac{1}{\text{to} - \text{from}}
        """
        pass

    def unsqueeze(self, dim): # real signature unknown; restored from __doc__
        """
        unsqueeze(dim) -> Tensor
        
        See :func:`torch.unsqueeze`
        """
        pass

    def unsqueeze_(self, dim): # real signature unknown; restored from __doc__
        """
        unsqueeze_(dim) -> Tensor
        
        In-place version of :meth:`~Tensor.unsqueeze`
        """
        pass

    def values(self): # real signature unknown; restored from __doc__
        """
        values() -> Tensor
        
        If :attr:`self` is a sparse COO tensor (i.e., with ``torch.sparse_coo`` layout),
        this returns a view of the contained values tensor. Otherwise, this throws an
        error.
        
        See also :meth:`Tensor.indices`.
        
        .. note::
          This method can only be called on a coalesced sparse tensor. See
          :meth:`Tensor.coalesce` for details.
        """
        pass

    def var(self, dim=None, unbiased=True, keepdim=False): # real signature unknown; restored from __doc__
        """
        var(dim=None, unbiased=True, keepdim=False) -> Tensor
        
        See :func:`torch.var`
        """
        pass

    def view(self, *shape): # real signature unknown; restored from __doc__
        """
        view(*shape) -> Tensor
        
        Returns a new tensor with the same data as the :attr:`self` tensor but of a
        different :attr:`shape`.
        
        The returned tensor shares the same data and must have the same number
        of elements, but may have a different size. For a tensor to be viewed, the new
        view size must be compatible with its original size and stride, i.e., each new
        view dimension must either be a subspace of an original dimension, or only span
        across original dimensions :math:`d, d+1, \dots, d+k` that satisfy the following
        contiguity-like condition that :math:`\forall i = 0, \dots, k-1`,
        
        .. math::
        
          \text{stride}[i] = \text{stride}[i+1] \times \text{size}[i+1]
        
        Otherwise, :meth:`contiguous` needs to be called before the tensor can be
        viewed. See also: :meth:`reshape`, which returns a view if the shapes are
        compatible, and copies (equivalent to calling :meth:`contiguous`) otherwise.
        
        Args:
            shape (torch.Size or int...): the desired size
        
        Example::
        
            >>> x = torch.randn(4, 4)
            >>> x.size()
            torch.Size([4, 4])
            >>> y = x.view(16)
            >>> y.size()
            torch.Size([16])
            >>> z = x.view(-1, 8)  # the size -1 is inferred from other dimensions
            >>> z.size()
            torch.Size([2, 8])
        
            >>> a = torch.randn(1, 2, 3, 4)
            >>> a.size()
            torch.Size([1, 2, 3, 4])
            >>> b = a.transpose(1, 2)  # Swaps 2nd and 3rd dimension
            >>> b.size()
            torch.Size([1, 3, 2, 4])
            >>> c = a.view(1, 3, 2, 4)  # Does not change tensor layout in memory
            >>> c.size()
            torch.Size([1, 3, 2, 4])
            >>> torch.equal(b, c)
            False
        """
        pass

    def view_as(self, other): # real signature unknown; restored from __doc__
        """
        view_as(other) -> Tensor
        
        View this tensor as the same size as :attr:`other`.
        ``self.view_as(other)`` is equivalent to ``self.view(other.size())``.
        
        Please see :meth:`~Tensor.view` for more information about ``view``.
        
        Args:
            other (:class:`torch.Tensor`): The result tensor has the same size
                as :attr:`other`.
        """
        pass

    def where(self, condition, y): # real signature unknown; restored from __doc__
        """
        where(condition, y) -> Tensor
        
        ``self.where(condition, y)`` is equivalent to ``torch.where(condition, self, y)``.
        See :func:`torch.where`
        """
        pass

    def zero_(self): # real signature unknown; restored from __doc__
        """
        zero_() -> Tensor
        
        Fills :attr:`self` tensor with zeros.
        """
        pass

    def _coalesced_(self, *args, **kwargs): # real signature unknown
        pass

    def _dimI(self, *args, **kwargs): # real signature unknown
        pass

    def _dimV(self, *args, **kwargs): # real signature unknown
        pass

    def _indices(self, *args, **kwargs): # real signature unknown
        pass

    def _is_view(self, *args, **kwargs): # real signature unknown
        pass

    def _make_subclass(self, *args, **kwargs): # real signature unknown
        pass

    def _nnz(self, *args, **kwargs): # real signature unknown
        pass

    def _values(self, *args, **kwargs): # real signature unknown
        pass

    def __add__(self, *args, **kwargs): # real signature unknown
        pass

    def __and__(self, *args, **kwargs): # real signature unknown
        pass

    def __bool__(self, *args, **kwargs): # real signature unknown
        pass

    def __delitem__(self, *args, **kwargs): # real signature unknown
        """ Delete self[key]. """
        pass

    def __div__(self, *args, **kwargs): # real signature unknown
        pass

    def __float__(self, *args, **kwargs): # real signature unknown
        pass

    def __getitem__(self, *args, **kwargs): # real signature unknown
        """ Return self[key]. """
        pass

    def __iadd__(self, *args, **kwargs): # real signature unknown
        pass

    def __iand__(self, *args, **kwargs): # real signature unknown
        pass

    def __idiv__(self, *args, **kwargs): # real signature unknown
        pass

    def __ilshift__(self, *args, **kwargs): # real signature unknown
        pass

    def __imul__(self, *args, **kwargs): # real signature unknown
        pass

    def __index__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __int__(self, *args, **kwargs): # real signature unknown
        pass

    def __invert__(self, *args, **kwargs): # real signature unknown
        pass

    def __ior__(self, *args, **kwargs): # real signature unknown
        pass

    def __irshift__(self, *args, **kwargs): # real signature unknown
        pass

    def __isub__(self, *args, **kwargs): # real signature unknown
        pass

    def __ixor__(self, *args, **kwargs): # real signature unknown
        pass

    def __len__(self, *args, **kwargs): # real signature unknown
        """ Return len(self). """
        pass

    def __long__(self, *args, **kwargs): # real signature unknown
        pass

    def __lshift__(self, *args, **kwargs): # real signature unknown
        pass

    def __matmul__(self, *args, **kwargs): # real signature unknown
        pass

    def __mod__(self, *args, **kwargs): # real signature unknown
        pass

    def __mul__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __nonzero__(self, *args, **kwargs): # real signature unknown
        pass

    def __or__(self, *args, **kwargs): # real signature unknown
        pass

    def __radd__(self, *args, **kwargs): # real signature unknown
        pass

    def __rmul__(self, *args, **kwargs): # real signature unknown
        pass

    def __rshift__(self, *args, **kwargs): # real signature unknown
        pass

    def __setitem__(self, *args, **kwargs): # real signature unknown
        """ Set self[key] to value. """
        pass

    def __sub__(self, *args, **kwargs): # real signature unknown
        pass

    def __truediv__(self, *args, **kwargs): # real signature unknown
        pass

    def __xor__(self, *args, **kwargs): # real signature unknown
        pass

    data = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    device = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
Is the :class:`torch.device` where this Tensor is.
"""

    dtype = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    grad = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
This attribute is ``None`` by default and becomes a Tensor the first time a call to
:func:`backward` computes gradients for ``self``.
The attribute will then contain the gradients computed and future calls to
:func:`backward` will accumulate (add) gradients into it.
"""

    grad_fn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    is_cuda = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
Is ``True`` if the Tensor is stored on the GPU, ``False`` otherwise.
"""

    is_leaf = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
All Tensors that have :attr:`requires_grad` which is ``False`` will be leaf Tensors by convention.

For Tensors that have :attr:`requires_grad` which is ``True``, they will be leaf Tensors if they were
created by the user. This means that they are not the result of an operation and so
:attr:`grad_fn` is None.

Only leaf Tensors will have their :attr:`grad` populated during a call to :func:`backward`.
To get :attr:`grad` populated for non-leaf Tensors, you can use :func:`retain_grad`.

Example::

    >>> a = torch.rand(10, requires_grad=True)
    >>> a.is_leaf
    True
    >>> b = torch.rand(10, requires_grad=True).cuda()
    >>> b.is_leaf
    False
    # b was created by the operation that cast a cpu Tensor into a cuda Tensor
    >>> c = torch.rand(10, requires_grad=True) + 2
    >>> c.is_leaf
    False
    # c was created by the addition operation
    >>> d = torch.rand(10).cuda()
    >>> d.is_leaf
    True
    # d does not require gradients and so has no operation creating it (that is tracked by the autograd engine)
    >>> e = torch.rand(10).cuda().requires_grad_()
    >>> e.is_leaf
    True
    # e requires gradients and has no operations creating it
    >>> f = torch.rand(10, requires_grad=True, device="cuda")
    >>> f.is_leaf
    True
    # f requires grad, has no operation creating it


"""

    is_mkldnn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    is_quantized = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    is_sparse = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    layout = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    names = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
Stores names for each of this tensor's dimensions.

``names[idx]`` corresponds to the name of tensor dimension ``idx``.
Names are either a string if the dimension is named or ``None`` if the
dimension is unnamed.

Dimension names may contain characters or underscore. Furthermore, a dimension
name must be a valid Python variable name (i.e., does not start with underscore).

Tensors may not have two named dimensions with the same name.

.. warning::
    The named tensor API is experimental and subject to change.

"""

    ndim = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
Alias for :meth:`~Tensor.dim()`
"""

    output_nr = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    requires_grad = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
Is ``True`` if gradients need to be computed for this Tensor, ``False`` otherwise.

.. note::

    The fact that gradients need to be computed for a Tensor do not mean that the :attr:`grad`
    attribute will be populated, see :attr:`is_leaf` for more details.

"""

    shape = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    T = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
Is this Tensor with its dimensions reversed.

If ``n`` is the number of dimensions in ``x``,
``x.T`` is equivalent to ``x.permute(n-1, n-2, ..., 0)``.
"""

    volatile = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _backward_hooks = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _base = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _cdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _grad = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _grad_fn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _version = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



