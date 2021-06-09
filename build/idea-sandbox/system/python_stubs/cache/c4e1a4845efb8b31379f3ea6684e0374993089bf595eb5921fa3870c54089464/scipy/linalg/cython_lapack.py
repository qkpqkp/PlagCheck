# encoding: utf-8
# module scipy.linalg.cython_lapack
# from C:\Users\Doly\Anaconda3\lib\site-packages\scipy\linalg\cython_lapack.cp37-win_amd64.pyd
# by generator 1.147
"""
LAPACK functions for Cython
===========================

Usable from Cython via::

    cimport scipy.linalg.cython_lapack

This module provides Cython-level wrappers for all primary routines included
in LAPACK 3.4.0 except for ``zcgesv`` since its interface is not consistent
from LAPACK 3.4.0 to 3.6.0. It also provides some of the
fixed-api auxiliary routines.

These wrappers do not check for alignment of arrays.
Alignment should be checked before these wrappers are used.

Raw function pointers (Fortran-style pointer arguments):

- cbbcsd
- cbdsqr
- cgbbrd
- cgbcon
- cgbequ
- cgbequb
- cgbrfs
- cgbsv
- cgbsvx
- cgbtf2
- cgbtrf
- cgbtrs
- cgebak
- cgebal
- cgebd2
- cgebrd
- cgecon
- cgeequ
- cgeequb
- cgees
- cgeesx
- cgeev
- cgeevx
- cgehd2
- cgehrd
- cgelq2
- cgelqf
- cgels
- cgelsd
- cgelss
- cgelsy
- cgemqrt
- cgeql2
- cgeqlf
- cgeqp3
- cgeqr2
- cgeqr2p
- cgeqrf
- cgeqrfp
- cgeqrt
- cgeqrt2
- cgeqrt3
- cgerfs
- cgerq2
- cgerqf
- cgesc2
- cgesdd
- cgesv
- cgesvd
- cgesvx
- cgetc2
- cgetf2
- cgetrf
- cgetri
- cgetrs
- cggbak
- cggbal
- cgges
- cggesx
- cggev
- cggevx
- cggglm
- cgghrd
- cgglse
- cggqrf
- cggrqf
- cgtcon
- cgtrfs
- cgtsv
- cgtsvx
- cgttrf
- cgttrs
- cgtts2
- chbev
- chbevd
- chbevx
- chbgst
- chbgv
- chbgvd
- chbgvx
- chbtrd
- checon
- cheequb
- cheev
- cheevd
- cheevr
- cheevx
- chegs2
- chegst
- chegv
- chegvd
- chegvx
- cherfs
- chesv
- chesvx
- cheswapr
- chetd2
- chetf2
- chetrd
- chetrf
- chetri
- chetri2
- chetri2x
- chetrs
- chetrs2
- chfrk
- chgeqz
- chla_transtype
- chpcon
- chpev
- chpevd
- chpevx
- chpgst
- chpgv
- chpgvd
- chpgvx
- chprfs
- chpsv
- chpsvx
- chptrd
- chptrf
- chptri
- chptrs
- chsein
- chseqr
- clabrd
- clacgv
- clacn2
- clacon
- clacp2
- clacpy
- clacrm
- clacrt
- cladiv
- claed0
- claed7
- claed8
- claein
- claesy
- claev2
- clag2z
- clags2
- clagtm
- clahef
- clahqr
- clahr2
- claic1
- clals0
- clalsa
- clalsd
- clangb
- clange
- clangt
- clanhb
- clanhe
- clanhf
- clanhp
- clanhs
- clanht
- clansb
- clansp
- clansy
- clantb
- clantp
- clantr
- clapll
- clapmr
- clapmt
- claqgb
- claqge
- claqhb
- claqhe
- claqhp
- claqp2
- claqps
- claqr0
- claqr1
- claqr2
- claqr3
- claqr4
- claqr5
- claqsb
- claqsp
- claqsy
- clar1v
- clar2v
- clarcm
- clarf
- clarfb
- clarfg
- clarfgp
- clarft
- clarfx
- clargv
- clarnv
- clarrv
- clartg
- clartv
- clarz
- clarzb
- clarzt
- clascl
- claset
- clasr
- classq
- claswp
- clasyf
- clatbs
- clatdf
- clatps
- clatrd
- clatrs
- clatrz
- clauu2
- clauum
- cpbcon
- cpbequ
- cpbrfs
- cpbstf
- cpbsv
- cpbsvx
- cpbtf2
- cpbtrf
- cpbtrs
- cpftrf
- cpftri
- cpftrs
- cpocon
- cpoequ
- cpoequb
- cporfs
- cposv
- cposvx
- cpotf2
- cpotrf
- cpotri
- cpotrs
- cppcon
- cppequ
- cpprfs
- cppsv
- cppsvx
- cpptrf
- cpptri
- cpptrs
- cpstf2
- cpstrf
- cptcon
- cpteqr
- cptrfs
- cptsv
- cptsvx
- cpttrf
- cpttrs
- cptts2
- crot
- cspcon
- cspmv
- cspr
- csprfs
- cspsv
- cspsvx
- csptrf
- csptri
- csptrs
- csrscl
- cstedc
- cstegr
- cstein
- cstemr
- csteqr
- csycon
- csyconv
- csyequb
- csymv
- csyr
- csyrfs
- csysv
- csysvx
- csyswapr
- csytf2
- csytrf
- csytri
- csytri2
- csytri2x
- csytrs
- csytrs2
- ctbcon
- ctbrfs
- ctbtrs
- ctfsm
- ctftri
- ctfttp
- ctfttr
- ctgevc
- ctgex2
- ctgexc
- ctgsen
- ctgsja
- ctgsna
- ctgsy2
- ctgsyl
- ctpcon
- ctpmqrt
- ctpqrt
- ctpqrt2
- ctprfb
- ctprfs
- ctptri
- ctptrs
- ctpttf
- ctpttr
- ctrcon
- ctrevc
- ctrexc
- ctrrfs
- ctrsen
- ctrsna
- ctrsyl
- ctrti2
- ctrtri
- ctrtrs
- ctrttf
- ctrttp
- ctzrzf
- cunbdb
- cuncsd
- cung2l
- cung2r
- cungbr
- cunghr
- cungl2
- cunglq
- cungql
- cungqr
- cungr2
- cungrq
- cungtr
- cunm2l
- cunm2r
- cunmbr
- cunmhr
- cunml2
- cunmlq
- cunmql
- cunmqr
- cunmr2
- cunmr3
- cunmrq
- cunmrz
- cunmtr
- cupgtr
- cupmtr
- dbbcsd
- dbdsdc
- dbdsqr
- ddisna
- dgbbrd
- dgbcon
- dgbequ
- dgbequb
- dgbrfs
- dgbsv
- dgbsvx
- dgbtf2
- dgbtrf
- dgbtrs
- dgebak
- dgebal
- dgebd2
- dgebrd
- dgecon
- dgeequ
- dgeequb
- dgees
- dgeesx
- dgeev
- dgeevx
- dgehd2
- dgehrd
- dgejsv
- dgelq2
- dgelqf
- dgels
- dgelsd
- dgelss
- dgelsy
- dgemqrt
- dgeql2
- dgeqlf
- dgeqp3
- dgeqr2
- dgeqr2p
- dgeqrf
- dgeqrfp
- dgeqrt
- dgeqrt2
- dgeqrt3
- dgerfs
- dgerq2
- dgerqf
- dgesc2
- dgesdd
- dgesv
- dgesvd
- dgesvj
- dgesvx
- dgetc2
- dgetf2
- dgetrf
- dgetri
- dgetrs
- dggbak
- dggbal
- dgges
- dggesx
- dggev
- dggevx
- dggglm
- dgghrd
- dgglse
- dggqrf
- dggrqf
- dgsvj0
- dgsvj1
- dgtcon
- dgtrfs
- dgtsv
- dgtsvx
- dgttrf
- dgttrs
- dgtts2
- dhgeqz
- dhsein
- dhseqr
- disnan
- dlabad
- dlabrd
- dlacn2
- dlacon
- dlacpy
- dladiv
- dlae2
- dlaebz
- dlaed0
- dlaed1
- dlaed2
- dlaed3
- dlaed4
- dlaed5
- dlaed6
- dlaed7
- dlaed8
- dlaed9
- dlaeda
- dlaein
- dlaev2
- dlaexc
- dlag2
- dlag2s
- dlags2
- dlagtf
- dlagtm
- dlagts
- dlagv2
- dlahqr
- dlahr2
- dlaic1
- dlaln2
- dlals0
- dlalsa
- dlalsd
- dlamch
- dlamrg
- dlaneg
- dlangb
- dlange
- dlangt
- dlanhs
- dlansb
- dlansf
- dlansp
- dlanst
- dlansy
- dlantb
- dlantp
- dlantr
- dlanv2
- dlapll
- dlapmr
- dlapmt
- dlapy2
- dlapy3
- dlaqgb
- dlaqge
- dlaqp2
- dlaqps
- dlaqr0
- dlaqr1
- dlaqr2
- dlaqr3
- dlaqr4
- dlaqr5
- dlaqsb
- dlaqsp
- dlaqsy
- dlaqtr
- dlar1v
- dlar2v
- dlarf
- dlarfb
- dlarfg
- dlarfgp
- dlarft
- dlarfx
- dlargv
- dlarnv
- dlarra
- dlarrb
- dlarrc
- dlarrd
- dlarre
- dlarrf
- dlarrj
- dlarrk
- dlarrr
- dlarrv
- dlartg
- dlartgp
- dlartgs
- dlartv
- dlaruv
- dlarz
- dlarzb
- dlarzt
- dlas2
- dlascl
- dlasd0
- dlasd1
- dlasd2
- dlasd3
- dlasd4
- dlasd5
- dlasd6
- dlasd7
- dlasd8
- dlasda
- dlasdq
- dlasdt
- dlaset
- dlasq1
- dlasq2
- dlasq3
- dlasq4
- dlasq6
- dlasr
- dlasrt
- dlassq
- dlasv2
- dlaswp
- dlasy2
- dlasyf
- dlat2s
- dlatbs
- dlatdf
- dlatps
- dlatrd
- dlatrs
- dlatrz
- dlauu2
- dlauum
- dopgtr
- dopmtr
- dorbdb
- dorcsd
- dorg2l
- dorg2r
- dorgbr
- dorghr
- dorgl2
- dorglq
- dorgql
- dorgqr
- dorgr2
- dorgrq
- dorgtr
- dorm2l
- dorm2r
- dormbr
- dormhr
- dorml2
- dormlq
- dormql
- dormqr
- dormr2
- dormr3
- dormrq
- dormrz
- dormtr
- dpbcon
- dpbequ
- dpbrfs
- dpbstf
- dpbsv
- dpbsvx
- dpbtf2
- dpbtrf
- dpbtrs
- dpftrf
- dpftri
- dpftrs
- dpocon
- dpoequ
- dpoequb
- dporfs
- dposv
- dposvx
- dpotf2
- dpotrf
- dpotri
- dpotrs
- dppcon
- dppequ
- dpprfs
- dppsv
- dppsvx
- dpptrf
- dpptri
- dpptrs
- dpstf2
- dpstrf
- dptcon
- dpteqr
- dptrfs
- dptsv
- dptsvx
- dpttrf
- dpttrs
- dptts2
- drscl
- dsbev
- dsbevd
- dsbevx
- dsbgst
- dsbgv
- dsbgvd
- dsbgvx
- dsbtrd
- dsfrk
- dsgesv
- dspcon
- dspev
- dspevd
- dspevx
- dspgst
- dspgv
- dspgvd
- dspgvx
- dsposv
- dsprfs
- dspsv
- dspsvx
- dsptrd
- dsptrf
- dsptri
- dsptrs
- dstebz
- dstedc
- dstegr
- dstein
- dstemr
- dsteqr
- dsterf
- dstev
- dstevd
- dstevr
- dstevx
- dsycon
- dsyconv
- dsyequb
- dsyev
- dsyevd
- dsyevr
- dsyevx
- dsygs2
- dsygst
- dsygv
- dsygvd
- dsygvx
- dsyrfs
- dsysv
- dsysvx
- dsyswapr
- dsytd2
- dsytf2
- dsytrd
- dsytrf
- dsytri
- dsytri2
- dsytri2x
- dsytrs
- dsytrs2
- dtbcon
- dtbrfs
- dtbtrs
- dtfsm
- dtftri
- dtfttp
- dtfttr
- dtgevc
- dtgex2
- dtgexc
- dtgsen
- dtgsja
- dtgsna
- dtgsy2
- dtgsyl
- dtpcon
- dtpmqrt
- dtpqrt
- dtpqrt2
- dtprfb
- dtprfs
- dtptri
- dtptrs
- dtpttf
- dtpttr
- dtrcon
- dtrevc
- dtrexc
- dtrrfs
- dtrsen
- dtrsna
- dtrsyl
- dtrti2
- dtrtri
- dtrtrs
- dtrttf
- dtrttp
- dtzrzf
- dzsum1
- icmax1
- ieeeck
- ilaclc
- ilaclr
- iladiag
- iladlc
- iladlr
- ilaprec
- ilaslc
- ilaslr
- ilatrans
- ilauplo
- ilaver
- ilazlc
- ilazlr
- izmax1
- sbbcsd
- sbdsdc
- sbdsqr
- scsum1
- sdisna
- sgbbrd
- sgbcon
- sgbequ
- sgbequb
- sgbrfs
- sgbsv
- sgbsvx
- sgbtf2
- sgbtrf
- sgbtrs
- sgebak
- sgebal
- sgebd2
- sgebrd
- sgecon
- sgeequ
- sgeequb
- sgees
- sgeesx
- sgeev
- sgeevx
- sgehd2
- sgehrd
- sgejsv
- sgelq2
- sgelqf
- sgels
- sgelsd
- sgelss
- sgelsy
- sgemqrt
- sgeql2
- sgeqlf
- sgeqp3
- sgeqr2
- sgeqr2p
- sgeqrf
- sgeqrfp
- sgeqrt
- sgeqrt2
- sgeqrt3
- sgerfs
- sgerq2
- sgerqf
- sgesc2
- sgesdd
- sgesv
- sgesvd
- sgesvj
- sgesvx
- sgetc2
- sgetf2
- sgetrf
- sgetri
- sgetrs
- sggbak
- sggbal
- sgges
- sggesx
- sggev
- sggevx
- sggglm
- sgghrd
- sgglse
- sggqrf
- sggrqf
- sgsvj0
- sgsvj1
- sgtcon
- sgtrfs
- sgtsv
- sgtsvx
- sgttrf
- sgttrs
- sgtts2
- shgeqz
- shsein
- shseqr
- slabad
- slabrd
- slacn2
- slacon
- slacpy
- sladiv
- slae2
- slaebz
- slaed0
- slaed1
- slaed2
- slaed3
- slaed4
- slaed5
- slaed6
- slaed7
- slaed8
- slaed9
- slaeda
- slaein
- slaev2
- slaexc
- slag2
- slag2d
- slags2
- slagtf
- slagtm
- slagts
- slagv2
- slahqr
- slahr2
- slaic1
- slaln2
- slals0
- slalsa
- slalsd
- slamch
- slamrg
- slangb
- slange
- slangt
- slanhs
- slansb
- slansf
- slansp
- slanst
- slansy
- slantb
- slantp
- slantr
- slanv2
- slapll
- slapmr
- slapmt
- slapy2
- slapy3
- slaqgb
- slaqge
- slaqp2
- slaqps
- slaqr0
- slaqr1
- slaqr2
- slaqr3
- slaqr4
- slaqr5
- slaqsb
- slaqsp
- slaqsy
- slaqtr
- slar1v
- slar2v
- slarf
- slarfb
- slarfg
- slarfgp
- slarft
- slarfx
- slargv
- slarnv
- slarra
- slarrb
- slarrc
- slarrd
- slarre
- slarrf
- slarrj
- slarrk
- slarrr
- slarrv
- slartg
- slartgp
- slartgs
- slartv
- slaruv
- slarz
- slarzb
- slarzt
- slas2
- slascl
- slasd0
- slasd1
- slasd2
- slasd3
- slasd4
- slasd5
- slasd6
- slasd7
- slasd8
- slasda
- slasdq
- slasdt
- slaset
- slasq1
- slasq2
- slasq3
- slasq4
- slasq6
- slasr
- slasrt
- slassq
- slasv2
- slaswp
- slasy2
- slasyf
- slatbs
- slatdf
- slatps
- slatrd
- slatrs
- slatrz
- slauu2
- slauum
- sopgtr
- sopmtr
- sorbdb
- sorcsd
- sorg2l
- sorg2r
- sorgbr
- sorghr
- sorgl2
- sorglq
- sorgql
- sorgqr
- sorgr2
- sorgrq
- sorgtr
- sorm2l
- sorm2r
- sormbr
- sormhr
- sorml2
- sormlq
- sormql
- sormqr
- sormr2
- sormr3
- sormrq
- sormrz
- sormtr
- spbcon
- spbequ
- spbrfs
- spbstf
- spbsv
- spbsvx
- spbtf2
- spbtrf
- spbtrs
- spftrf
- spftri
- spftrs
- spocon
- spoequ
- spoequb
- sporfs
- sposv
- sposvx
- spotf2
- spotrf
- spotri
- spotrs
- sppcon
- sppequ
- spprfs
- sppsv
- sppsvx
- spptrf
- spptri
- spptrs
- spstf2
- spstrf
- sptcon
- spteqr
- sptrfs
- sptsv
- sptsvx
- spttrf
- spttrs
- sptts2
- srscl
- ssbev
- ssbevd
- ssbevx
- ssbgst
- ssbgv
- ssbgvd
- ssbgvx
- ssbtrd
- ssfrk
- sspcon
- sspev
- sspevd
- sspevx
- sspgst
- sspgv
- sspgvd
- sspgvx
- ssprfs
- sspsv
- sspsvx
- ssptrd
- ssptrf
- ssptri
- ssptrs
- sstebz
- sstedc
- sstegr
- sstein
- sstemr
- ssteqr
- ssterf
- sstev
- sstevd
- sstevr
- sstevx
- ssycon
- ssyconv
- ssyequb
- ssyev
- ssyevd
- ssyevr
- ssyevx
- ssygs2
- ssygst
- ssygv
- ssygvd
- ssygvx
- ssyrfs
- ssysv
- ssysvx
- ssyswapr
- ssytd2
- ssytf2
- ssytrd
- ssytrf
- ssytri
- ssytri2
- ssytri2x
- ssytrs
- ssytrs2
- stbcon
- stbrfs
- stbtrs
- stfsm
- stftri
- stfttp
- stfttr
- stgevc
- stgex2
- stgexc
- stgsen
- stgsja
- stgsna
- stgsy2
- stgsyl
- stpcon
- stpmqrt
- stpqrt
- stpqrt2
- stprfb
- stprfs
- stptri
- stptrs
- stpttf
- stpttr
- strcon
- strevc
- strexc
- strrfs
- strsen
- strsna
- strsyl
- strti2
- strtri
- strtrs
- strttf
- strttp
- stzrzf
- xerbla_array
- zbbcsd
- zbdsqr
- zcgesv
- zcposv
- zdrscl
- zgbbrd
- zgbcon
- zgbequ
- zgbequb
- zgbrfs
- zgbsv
- zgbsvx
- zgbtf2
- zgbtrf
- zgbtrs
- zgebak
- zgebal
- zgebd2
- zgebrd
- zgecon
- zgeequ
- zgeequb
- zgees
- zgeesx
- zgeev
- zgeevx
- zgehd2
- zgehrd
- zgelq2
- zgelqf
- zgels
- zgelsd
- zgelss
- zgelsy
- zgemqrt
- zgeql2
- zgeqlf
- zgeqp3
- zgeqr2
- zgeqr2p
- zgeqrf
- zgeqrfp
- zgeqrt
- zgeqrt2
- zgeqrt3
- zgerfs
- zgerq2
- zgerqf
- zgesc2
- zgesdd
- zgesv
- zgesvd
- zgesvx
- zgetc2
- zgetf2
- zgetrf
- zgetri
- zgetrs
- zggbak
- zggbal
- zgges
- zggesx
- zggev
- zggevx
- zggglm
- zgghrd
- zgglse
- zggqrf
- zggrqf
- zgtcon
- zgtrfs
- zgtsv
- zgtsvx
- zgttrf
- zgttrs
- zgtts2
- zhbev
- zhbevd
- zhbevx
- zhbgst
- zhbgv
- zhbgvd
- zhbgvx
- zhbtrd
- zhecon
- zheequb
- zheev
- zheevd
- zheevr
- zheevx
- zhegs2
- zhegst
- zhegv
- zhegvd
- zhegvx
- zherfs
- zhesv
- zhesvx
- zheswapr
- zhetd2
- zhetf2
- zhetrd
- zhetrf
- zhetri
- zhetri2
- zhetri2x
- zhetrs
- zhetrs2
- zhfrk
- zhgeqz
- zhpcon
- zhpev
- zhpevd
- zhpevx
- zhpgst
- zhpgv
- zhpgvd
- zhpgvx
- zhprfs
- zhpsv
- zhpsvx
- zhptrd
- zhptrf
- zhptri
- zhptrs
- zhsein
- zhseqr
- zlabrd
- zlacgv
- zlacn2
- zlacon
- zlacp2
- zlacpy
- zlacrm
- zlacrt
- zladiv
- zlaed0
- zlaed7
- zlaed8
- zlaein
- zlaesy
- zlaev2
- zlag2c
- zlags2
- zlagtm
- zlahef
- zlahqr
- zlahr2
- zlaic1
- zlals0
- zlalsa
- zlalsd
- zlangb
- zlange
- zlangt
- zlanhb
- zlanhe
- zlanhf
- zlanhp
- zlanhs
- zlanht
- zlansb
- zlansp
- zlansy
- zlantb
- zlantp
- zlantr
- zlapll
- zlapmr
- zlapmt
- zlaqgb
- zlaqge
- zlaqhb
- zlaqhe
- zlaqhp
- zlaqp2
- zlaqps
- zlaqr0
- zlaqr1
- zlaqr2
- zlaqr3
- zlaqr4
- zlaqr5
- zlaqsb
- zlaqsp
- zlaqsy
- zlar1v
- zlar2v
- zlarcm
- zlarf
- zlarfb
- zlarfg
- zlarfgp
- zlarft
- zlarfx
- zlargv
- zlarnv
- zlarrv
- zlartg
- zlartv
- zlarz
- zlarzb
- zlarzt
- zlascl
- zlaset
- zlasr
- zlassq
- zlaswp
- zlasyf
- zlat2c
- zlatbs
- zlatdf
- zlatps
- zlatrd
- zlatrs
- zlatrz
- zlauu2
- zlauum
- zpbcon
- zpbequ
- zpbrfs
- zpbstf
- zpbsv
- zpbsvx
- zpbtf2
- zpbtrf
- zpbtrs
- zpftrf
- zpftri
- zpftrs
- zpocon
- zpoequ
- zpoequb
- zporfs
- zposv
- zposvx
- zpotf2
- zpotrf
- zpotri
- zpotrs
- zppcon
- zppequ
- zpprfs
- zppsv
- zppsvx
- zpptrf
- zpptri
- zpptrs
- zpstf2
- zpstrf
- zptcon
- zpteqr
- zptrfs
- zptsv
- zptsvx
- zpttrf
- zpttrs
- zptts2
- zrot
- zspcon
- zspmv
- zspr
- zsprfs
- zspsv
- zspsvx
- zsptrf
- zsptri
- zsptrs
- zstedc
- zstegr
- zstein
- zstemr
- zsteqr
- zsycon
- zsyconv
- zsyequb
- zsymv
- zsyr
- zsyrfs
- zsysv
- zsysvx
- zsyswapr
- zsytf2
- zsytrf
- zsytri
- zsytri2
- zsytri2x
- zsytrs
- zsytrs2
- ztbcon
- ztbrfs
- ztbtrs
- ztfsm
- ztftri
- ztfttp
- ztfttr
- ztgevc
- ztgex2
- ztgexc
- ztgsen
- ztgsja
- ztgsna
- ztgsy2
- ztgsyl
- ztpcon
- ztpmqrt
- ztpqrt
- ztpqrt2
- ztprfb
- ztprfs
- ztptri
- ztptrs
- ztpttf
- ztpttr
- ztrcon
- ztrevc
- ztrexc
- ztrrfs
- ztrsen
- ztrsna
- ztrsyl
- ztrti2
- ztrtri
- ztrtrs
- ztrttf
- ztrttp
- ztzrzf
- zunbdb
- zuncsd
- zung2l
- zung2r
- zungbr
- zunghr
- zungl2
- zunglq
- zungql
- zungqr
- zungr2
- zungrq
- zungtr
- zunm2l
- zunm2r
- zunmbr
- zunmhr
- zunml2
- zunmlq
- zunmql
- zunmqr
- zunmr2
- zunmr3
- zunmrq
- zunmrz
- zunmtr
- zupgtr
- zupmtr
"""

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>

# functions

def _test_dlamch(*args, **kwargs): # real signature unknown
    pass

def _test_slamch(*args, **kwargs): # real signature unknown
    pass

# no classes
# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x0000019E936CBF28>'

__pyx_capi__ = {
    'cbbcsd': None, # (!) real value is '<capsule object "void (char *, char *, char *, char *, char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x0000019E936D06C0>'
    'cbdsqr': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E936D06F0>'
    'cgbbrd': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E936D0720>'
    'cgbcon': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, __pyx_t_float_complex *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E936D0750>'
    'cgbequ': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E936D0780>'
    'cgbequb': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E936D07B0>'
    'cgbrfs': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E936D07E0>'
    'cgbsv': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, __pyx_t_float_complex *, int *, int *, __pyx_t_float_complex *, int *, int *)" at 0x0000019E936D0810>'
    'cgbsvx': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, int *, char *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E936D0840>'
    'cgbtf2': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, __pyx_t_float_complex *, int *, int *, int *)" at 0x0000019E936D0870>'
    'cgbtrf': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, __pyx_t_float_complex *, int *, int *, int *)" at 0x0000019E936D08A0>'
    'cgbtrs': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, int *, __pyx_t_float_complex *, int *, int *, __pyx_t_float_complex *, int *, int *)" at 0x0000019E936D08D0>'
    'cgebak': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_float_complex *, int *, int *)" at 0x0000019E936D0900>'
    'cgebal': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_float_complex *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E936D0930>'
    'cgebd2': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *)" at 0x0000019E936D0960>'
    'cgebrd': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, int *)" at 0x0000019E936D0990>'
    'cgecon': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E936D09C0>'
    'cgeequ': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E936D09F0>'
    'cgeequb': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E936D0A20>'
    'cgees': None, # (!) real value is '<capsule object "void (char *, char *, __pyx_t_5scipy_6linalg_13cython_lapack_cselect1 *, int *, __pyx_t_float_complex *, int *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x0000019E936D0A50>'
    'cgeesx': None, # (!) real value is '<capsule object "void (char *, char *, __pyx_t_5scipy_6linalg_13cython_lapack_cselect1 *, char *, int *, __pyx_t_float_complex *, int *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x0000019E936D0A80>'
    'cgeev': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E936D0AB0>'
    'cgeevx': None, # (!) real value is '<capsule object "void (char *, char *, char *, char *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E936D0AE0>'
    'cgehd2': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *)" at 0x0000019E936D0B10>'
    'cgehrd': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, int *)" at 0x0000019E936D0B40>'
    'cgelq2': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *)" at 0x0000019E936D0B70>'
    'cgelqf': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, int *)" at 0x0000019E936D0BA0>'
    'cgels': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, int *)" at 0x0000019E936D0BD0>'
    'cgelsd': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x0000019E936D0C00>'
    'cgelss': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E936D0C30>'
    'cgelsy': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E936D0C60>'
    'cgemqrt': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *)" at 0x0000019E936D0C90>'
    'cgeql2': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *)" at 0x0000019E936D0CC0>'
    'cgeqlf': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, int *)" at 0x0000019E936D0CF0>'
    'cgeqp3': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_float_complex *, int *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E936D0D20>'
    'cgeqr2': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *)" at 0x0000019E936D0D50>'
    'cgeqr2p': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *)" at 0x0000019E936D0D80>'
    'cgeqrf': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, int *)" at 0x0000019E936D0DB0>'
    'cgeqrfp': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, int *)" at 0x0000019E936D0DE0>'
    'cgeqrt': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *)" at 0x0000019E936D0E10>'
    'cgeqrt2': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, int *)" at 0x0000019E936D0E40>'
    'cgeqrt3': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, int *)" at 0x0000019E936D0E70>'
    'cgerfs': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E936D0EA0>'
    'cgerq2': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *)" at 0x0000019E936D0ED0>'
    'cgerqf': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, int *)" at 0x0000019E936D0F00>'
    'cgesc2': None, # (!) real value is '<capsule object "void (int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0x0000019E936D0F30>'
    'cgesdd': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x0000019E936D0F60>'
    'cgesv': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_float_complex *, int *, int *, __pyx_t_float_complex *, int *, int *)" at 0x0000019E936D0F90>'
    'cgesvd': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E936D0FC0>'
    'cgesvx': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, int *, char *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E936D3030>'
    'cgetc2': None, # (!) real value is '<capsule object "void (int *, __pyx_t_float_complex *, int *, int *, int *, int *)" at 0x0000019E936D3060>'
    'cgetf2': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_float_complex *, int *, int *, int *)" at 0x0000019E936D3090>'
    'cgetrf': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_float_complex *, int *, int *, int *)" at 0x0000019E936D30C0>'
    'cgetri': None, # (!) real value is '<capsule object "void (int *, __pyx_t_float_complex *, int *, int *, __pyx_t_float_complex *, int *, int *)" at 0x0000019E936D30F0>'
    'cgetrs': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_float_complex *, int *, int *, __pyx_t_float_complex *, int *, int *)" at 0x0000019E936D3120>'
    'cggbak': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_float_complex *, int *, int *)" at 0x0000019E936D3150>'
    'cggbal': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E936D3180>'
    'cgges': None, # (!) real value is '<capsule object "void (char *, char *, char *, __pyx_t_5scipy_6linalg_13cython_lapack_cselect2 *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x0000019E936D31B0>'
    'cggesx': None, # (!) real value is '<capsule object "void (char *, char *, char *, __pyx_t_5scipy_6linalg_13cython_lapack_cselect2 *, char *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, int *)" at 0x0000019E936D31E0>'
    'cggev': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E936D3210>'
    'cggevx': None, # (!) real value is '<capsule object "void (char *, char *, char *, char *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *)" at 0x0000019E936D3240>'
    'cggglm': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, int *)" at 0x0000019E936D3270>'
    'cgghrd': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, int *)" at 0x0000019E936D32A0>'
    'cgglse': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, int *)" at 0x0000019E936D32D0>'
    'cggqrf': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, int *)" at 0x0000019E936D3300>'
    'cggrqf': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, int *)" at 0x0000019E936D3330>'
    'cgtcon': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *)" at 0x0000019E936D3360>'
    'cgtrfs': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E936D3390>'
    'cgtsv': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, int *)" at 0x0000019E936D33C0>'
    'cgtsvx': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E936D33F0>'
    'cgttrf': None, # (!) real value is '<capsule object "void (int *, __pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, int *)" at 0x0000019E936D3420>'
    'cgttrs': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, int *)" at 0x0000019E936D3450>'
    'cgtts2': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *)" at 0x0000019E936D3480>'
    'chbev': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E936D34B0>'
    'chbevd': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, int *)" at 0x0000019E936D34E0>'
    'chbevx': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *)" at 0x0000019E936D3510>'
    'chbgst': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E936D3540>'
    'chbgv': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E936D3570>'
    'chbgvd': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, int *)" at 0x0000019E936D35A0>'
    'chbgvx': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *)" at 0x0000019E936D35D0>'
    'chbtrd': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *)" at 0x0000019E936D3600>'
    'checon': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_float_complex *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *)" at 0x0000019E936D3630>'
    'cheequb': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *)" at 0x0000019E936D3660>'
    'cheev': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E936D3690>'
    'cheevd': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, int *)" at 0x0000019E936D36C0>'
    'cheevr': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, int *)" at 0x0000019E936D36F0>'
    'cheevx': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *)" at 0x0000019E936D3720>'
    'chegs2': None, # (!) real value is '<capsule object "void (int *, char *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, int *)" at 0x0000019E936D3750>'
    'chegst': None, # (!) real value is '<capsule object "void (int *, char *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, int *)" at 0x0000019E936D3780>'
    'chegv': None, # (!) real value is '<capsule object "void (int *, char *, char *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E936D37B0>'
    'chegvd': None, # (!) real value is '<capsule object "void (int *, char *, char *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, int *)" at 0x0000019E936D37E0>'
    'chegvx': None, # (!) real value is '<capsule object "void (int *, char *, char *, char *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *)" at 0x0000019E936D3810>'
    'cherfs': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E936D3840>'
    'chesv': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_float_complex *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, int *)" at 0x0000019E936D3870>'
    'chesvx': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E936D38A0>'
    'cheswapr': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_float_complex *, int *, int *, int *)" at 0x0000019E936D38D0>'
    'chetd2': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *)" at 0x0000019E936D3900>'
    'chetf2': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_float_complex *, int *, int *, int *)" at 0x0000019E936D3930>'
    'chetrd': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, int *)" at 0x0000019E936D3960>'
    'chetrf': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_float_complex *, int *, int *, __pyx_t_float_complex *, int *, int *)" at 0x0000019E936D3990>'
    'chetri': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_float_complex *, int *, int *, __pyx_t_float_complex *, int *)" at 0x0000019E936D39C0>'
    'chetri2': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_float_complex *, int *, int *, __pyx_t_float_complex *, int *, int *)" at 0x0000019E936D39F0>'
    'chetri2x': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_float_complex *, int *, int *, __pyx_t_float_complex *, int *, int *)" at 0x0000019E936D3A20>'
    'chetrs': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_float_complex *, int *, int *, __pyx_t_float_complex *, int *, int *)" at 0x0000019E936D3A50>'
    'chetrs2': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_float_complex *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *)" at 0x0000019E936D3A80>'
    'chfrk': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *)" at 0x0000019E936D3AB0>'
    'chgeqz': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E936D3AE0>'
    'chla_transtype': None, # (!) real value is '<capsule object "char (int *)" at 0x0000019E936D3B10>'
    'chpcon': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *)" at 0x0000019E936D3B40>'
    'chpev': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E936D3B70>'
    'chpevd': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, int *)" at 0x0000019E936D3BA0>'
    'chpevx': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *)" at 0x0000019E936D3BD0>'
    'chpgst': None, # (!) real value is '<capsule object "void (int *, char *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *)" at 0x0000019E936D3C00>'
    'chpgv': None, # (!) real value is '<capsule object "void (int *, char *, char *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E936D3C30>'
    'chpgvd': None, # (!) real value is '<capsule object "void (int *, char *, char *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, int *)" at 0x0000019E936D3C60>'
    'chpgvx': None, # (!) real value is '<capsule object "void (int *, char *, char *, char *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *)" at 0x0000019E936D3C90>'
    'chprfs': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E936D3CC0>'
    'chpsv': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, int *)" at 0x0000019E936D3CF0>'
    'chpsvx': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E936D3D20>'
    'chptrd': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *)" at 0x0000019E936D3D50>'
    'chptrf': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_float_complex *, int *, int *)" at 0x0000019E936D3D80>'
    'chptri': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *)" at 0x0000019E936D3DB0>'
    'chptrs': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, int *)" at 0x0000019E936D3DE0>'
    'chsein': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, int *, int *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *)" at 0x0000019E936D3E10>'
    'chseqr': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, int *)" at 0x0000019E936D3E40>'
    'clabrd': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *)" at 0x0000019E936D3E70>'
    'clacgv': None, # (!) real value is '<capsule object "void (int *, __pyx_t_float_complex *, int *)" at 0x0000019E936D3EA0>'
    'clacn2': None, # (!) real value is '<capsule object "void (int *, __pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x0000019E936D3ED0>'
    'clacon': None, # (!) real value is '<capsule object "void (int *, __pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E936D3F00>'
    'clacp2': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_float_complex *, int *)" at 0x0000019E936D3F30>'
    'clacpy': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *)" at 0x0000019E936D3F60>'
    'clacrm': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0x0000019E936D3F90>'
    'clacrt': None, # (!) real value is '<capsule object "void (int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *)" at 0x0000019E936D3FC0>'
    'cladiv': None, # (!) real value is '<capsule object "__pyx_t_float_complex (__pyx_t_float_complex *, __pyx_t_float_complex *)" at 0x0000019E936D5030>'
    'claed0': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x0000019E936D5060>'
    'claed7': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x0000019E936D5090>'
    'claed8': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E936D50C0>'
    'claein': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E936D50F0>'
    'claesy': None, # (!) real value is '<capsule object "void (__pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_float_complex *)" at 0x0000019E936D5120>'
    'claev2': None, # (!) real value is '<capsule object "void (__pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *)" at 0x0000019E936D5150>'
    'clag2z': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_float_complex *, int *, __pyx_t_double_complex *, int *, int *)" at 0x0000019E936D5180>'
    'clags2': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *)" at 0x0000019E936D51B0>'
    'clagtm': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *)" at 0x0000019E936D51E0>'
    'clahef': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, __pyx_t_float_complex *, int *, int *, __pyx_t_float_complex *, int *, int *)" at 0x0000019E936D5210>'
    'clahqr': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, int *, __pyx_t_float_complex *, int *, int *)" at 0x0000019E936D5240>'
    'clahr2': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *)" at 0x0000019E936D5270>'
    'claic1': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, __pyx_t_float_complex *)" at 0x0000019E936D52A0>'
    'clals0': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E936D52D0>'
    'clalsa': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x0000019E936D5300>'
    'clalsd': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x0000019E936D5330>'
    'clangb': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_13cython_lapack_s (char *, int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0x0000019E936D5360>'
    'clange': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_13cython_lapack_s (char *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0x0000019E936D5390>'
    'clangt': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_13cython_lapack_s (char *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_float_complex *)" at 0x0000019E936D53C0>'
    'clanhb': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_13cython_lapack_s (char *, char *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0x0000019E936D53F0>'
    'clanhe': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_13cython_lapack_s (char *, char *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0x0000019E936D5420>'
    'clanhf': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_13cython_lapack_s (char *, char *, char *, int *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0x0000019E936D5450>'
    'clanhp': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_13cython_lapack_s (char *, char *, int *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0x0000019E936D5480>'
    'clanhs': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_13cython_lapack_s (char *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0x0000019E936D54B0>'
    'clanht': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_13cython_lapack_s (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *)" at 0x0000019E936D54E0>'
    'clansb': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_13cython_lapack_s (char *, char *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0x0000019E936D5510>'
    'clansp': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_13cython_lapack_s (char *, char *, int *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0x0000019E936D5540>'
    'clansy': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_13cython_lapack_s (char *, char *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0x0000019E936D5570>'
    'clantb': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_13cython_lapack_s (char *, char *, char *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0x0000019E936D55A0>'
    'clantp': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_13cython_lapack_s (char *, char *, char *, int *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0x0000019E936D55D0>'
    'clantr': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_13cython_lapack_s (char *, char *, char *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0x0000019E936D5600>'
    'clapll': None, # (!) real value is '<capsule object "void (int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0x0000019E936D5630>'
    'clapmr': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_float_complex *, int *, int *)" at 0x0000019E936D5660>'
    'clapmt': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_float_complex *, int *, int *)" at 0x0000019E936D5690>'
    'claqgb': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, char *)" at 0x0000019E936D56C0>'
    'claqge': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, char *)" at 0x0000019E936D56F0>'
    'claqhb': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, char *)" at 0x0000019E936D5720>'
    'claqhe': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, char *)" at 0x0000019E936D5750>'
    'claqhp': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, char *)" at 0x0000019E936D5780>'
    'claqp2': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_float_complex *, int *, int *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *)" at 0x0000019E936D57B0>'
    'claqps': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, int *, __pyx_t_float_complex *, int *, int *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *)" at 0x0000019E936D57E0>'
    'claqr0': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, int *)" at 0x0000019E936D5810>'
    'claqr1': None, # (!) real value is '<capsule object "void (int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_float_complex *)" at 0x0000019E936D5840>'
    'claqr2': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, int *, int *, __pyx_t_float_complex *, int *, int *, int *, __pyx_t_float_complex *, int *, int *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, int *, __pyx_t_float_complex *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *)" at 0x0000019E936D5870>'
    'claqr3': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, int *, int *, __pyx_t_float_complex *, int *, int *, int *, __pyx_t_float_complex *, int *, int *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, int *, __pyx_t_float_complex *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *)" at 0x0000019E936D58A0>'
    'claqr4': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, int *)" at 0x0000019E936D58D0>'
    'claqr5': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, int *, int *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, int *, __pyx_t_float_complex *, int *, int *, __pyx_t_float_complex *, int *)" at 0x0000019E936D5900>'
    'claqsb': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, char *)" at 0x0000019E936D5930>'
    'claqsp': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, char *)" at 0x0000019E936D5960>'
    'claqsy': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, char *)" at 0x0000019E936D5990>'
    'clar1v': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0x0000019E936D59C0>'
    'clar2v': None, # (!) real value is '<capsule object "void (int *, __pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *)" at 0x0000019E936D59F0>'
    'clarcm': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0x0000019E936D5A20>'
    'clarf': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *)" at 0x0000019E936D5A50>'
    'clarfb': None, # (!) real value is '<capsule object "void (char *, char *, char *, char *, int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *)" at 0x0000019E936D5A80>'
    'clarfg': None, # (!) real value is '<capsule object "void (int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *)" at 0x0000019E936D5AB0>'
    'clarfgp': None, # (!) real value is '<capsule object "void (int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *)" at 0x0000019E936D5AE0>'
    'clarft': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *)" at 0x0000019E936D5B10>'
    'clarfx': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *)" at 0x0000019E936D5B40>'
    'clargv': None, # (!) real value is '<capsule object "void (int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E936D5B70>'
    'clarnv': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_float_complex *)" at 0x0000019E936D5BA0>'
    'clarrv': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x0000019E936D5BD0>'
    'clartg': None, # (!) real value is '<capsule object "void (__pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, __pyx_t_float_complex *)" at 0x0000019E936D5C00>'
    'clartv': None, # (!) real value is '<capsule object "void (int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *)" at 0x0000019E936D5C30>'
    'clarz': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *)" at 0x0000019E936D5C60>'
    'clarzb': None, # (!) real value is '<capsule object "void (char *, char *, char *, char *, int *, int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *)" at 0x0000019E936D5C90>'
    'clarzt': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *)" at 0x0000019E936D5CC0>'
    'clascl': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_float_complex *, int *, int *)" at 0x0000019E936D5CF0>'
    'claset': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *)" at 0x0000019E936D5D20>'
    'clasr': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *)" at 0x0000019E936D5D50>'
    'classq': None, # (!) real value is '<capsule object "void (int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0x0000019E936D5D80>'
    'claswp': None, # (!) real value is '<capsule object "void (int *, __pyx_t_float_complex *, int *, int *, int *, int *, int *)" at 0x0000019E936D5DB0>'
    'clasyf': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, __pyx_t_float_complex *, int *, int *, __pyx_t_float_complex *, int *, int *)" at 0x0000019E936D5DE0>'
    'clatbs': None, # (!) real value is '<capsule object "void (char *, char *, char *, char *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E936D5E10>'
    'clatdf': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x0000019E936D5E40>'
    'clatps': None, # (!) real value is '<capsule object "void (char *, char *, char *, char *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E936D5E70>'
    'clatrd': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *)" at 0x0000019E936D5EA0>'
    'clatrs': None, # (!) real value is '<capsule object "void (char *, char *, char *, char *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E936D5ED0>'
    'clatrz': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *)" at 0x0000019E936D5F00>'
    'clauu2': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_float_complex *, int *, int *)" at 0x0000019E936D5F30>'
    'clauum': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_float_complex *, int *, int *)" at 0x0000019E936D5F60>'
    'cpbcon': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E936D5F90>'
    'cpbequ': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E936D5FC0>'
    'cpbrfs': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E936D7030>'
    'cpbstf': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_float_complex *, int *, int *)" at 0x0000019E936D7060>'
    'cpbsv': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, int *)" at 0x0000019E936D7090>'
    'cpbsvx': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, char *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E936D70C0>'
    'cpbtf2': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_float_complex *, int *, int *)" at 0x0000019E936D70F0>'
    'cpbtrf': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_float_complex *, int *, int *)" at 0x0000019E936D7120>'
    'cpbtrs': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, int *)" at 0x0000019E936D7150>'
    'cpftrf': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_float_complex *, int *)" at 0x0000019E936D7180>'
    'cpftri': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_float_complex *, int *)" at 0x0000019E936D71B0>'
    'cpftrs': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, int *)" at 0x0000019E936D71E0>'
    'cpocon': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E936D7210>'
    'cpoequ': None, # (!) real value is '<capsule object "void (int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E936D7240>'
    'cpoequb': None, # (!) real value is '<capsule object "void (int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E936D7270>'
    'cporfs': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E936D72A0>'
    'cposv': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, int *)" at 0x0000019E936D72D0>'
    'cposvx': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, char *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E936D7300>'
    'cpotf2': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_float_complex *, int *, int *)" at 0x0000019E936D7330>'
    'cpotrf': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_float_complex *, int *, int *)" at 0x0000019E936D7360>'
    'cpotri': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_float_complex *, int *, int *)" at 0x0000019E936D7390>'
    'cpotrs': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, int *)" at 0x0000019E936D73C0>'
    'cppcon': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E936D73F0>'
    'cppequ': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E936D7420>'
    'cpprfs': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E936D7450>'
    'cppsv': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, int *)" at 0x0000019E936D7480>'
    'cppsvx': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, char *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E936D74B0>'
    'cpptrf': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_float_complex *, int *)" at 0x0000019E936D74E0>'
    'cpptri': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_float_complex *, int *)" at 0x0000019E936D7510>'
    'cpptrs': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, int *)" at 0x0000019E936D7540>'
    'cpstf2': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_float_complex *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E936D7570>'
    'cpstrf': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_float_complex *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E936D75A0>'
    'cptcon': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E936D75D0>'
    'cpteqr': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E936D7600>'
    'cptrfs': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E936D7630>'
    'cptsv': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, int *)" at 0x0000019E936D7660>'
    'cptsvx': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E936D7690>'
    'cpttrf': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *)" at 0x0000019E936D76C0>'
    'cpttrs': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, int *)" at 0x0000019E936D76F0>'
    'cptts2': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *)" at 0x0000019E936D7720>'
    'crot': None, # (!) real value is '<capsule object "void (int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *)" at 0x0000019E936D7750>'
    'cspcon': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *)" at 0x0000019E936D7780>'
    'cspmv': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *)" at 0x0000019E936D77B0>'
    'cspr': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *)" at 0x0000019E936D77E0>'
    'csprfs': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E936D7810>'
    'cspsv': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, int *)" at 0x0000019E936D7840>'
    'cspsvx': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E936D7870>'
    'csptrf': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_float_complex *, int *, int *)" at 0x0000019E936D78A0>'
    'csptri': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *)" at 0x0000019E936D78D0>'
    'csptrs': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, int *)" at 0x0000019E936D7900>'
    'csrscl': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *)" at 0x0000019E936D7930>'
    'cstedc': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, int *)" at 0x0000019E936D7960>'
    'cstegr': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, int *)" at 0x0000019E936D7990>'
    'cstein': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *)" at 0x0000019E936D79C0>'
    'cstemr': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, int *)" at 0x0000019E936D79F0>'
    'csteqr': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E936D7A20>'
    'csycon': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_float_complex *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *)" at 0x0000019E936D7A50>'
    'csyconv': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_float_complex *, int *, int *, __pyx_t_float_complex *, int *)" at 0x0000019E936D7A80>'
    'csyequb': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *)" at 0x0000019E936D7AB0>'
    'csymv': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *)" at 0x0000019E936D7AE0>'
    'csyr': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *)" at 0x0000019E936D7B10>'
    'csyrfs': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E936D7B40>'
    'csysv': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_float_complex *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, int *)" at 0x0000019E936D7B70>'
    'csysvx': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E936D7BA0>'
    'csyswapr': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_float_complex *, int *, int *, int *)" at 0x0000019E936D7BD0>'
    'csytf2': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_float_complex *, int *, int *, int *)" at 0x0000019E936D7C00>'
    'csytrf': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_float_complex *, int *, int *, __pyx_t_float_complex *, int *, int *)" at 0x0000019E936D7C30>'
    'csytri': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_float_complex *, int *, int *, __pyx_t_float_complex *, int *)" at 0x0000019E936D7C60>'
    'csytri2': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_float_complex *, int *, int *, __pyx_t_float_complex *, int *, int *)" at 0x0000019E936D7C90>'
    'csytri2x': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_float_complex *, int *, int *, __pyx_t_float_complex *, int *, int *)" at 0x0000019E936D7CC0>'
    'csytrs': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_float_complex *, int *, int *, __pyx_t_float_complex *, int *, int *)" at 0x0000019E936D7CF0>'
    'csytrs2': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_float_complex *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *)" at 0x0000019E936D7D20>'
    'ctbcon': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E936D7D50>'
    'ctbrfs': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E936D7D80>'
    'ctbtrs': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, int *)" at 0x0000019E936D7DB0>'
    'ctfsm': None, # (!) real value is '<capsule object "void (char *, char *, char *, char *, char *, int *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *)" at 0x0000019E936D7DE0>'
    'ctftri': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, __pyx_t_float_complex *, int *)" at 0x0000019E936D7E10>'
    'ctfttp': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *)" at 0x0000019E936D7E40>'
    'ctfttr': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, int *)" at 0x0000019E936D7E70>'
    'ctgevc': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, int *, int *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E936D7EA0>'
    'ctgex2': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, int *, int *)" at 0x0000019E936D7ED0>'
    'ctgexc': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, int *, int *, int *)" at 0x0000019E936D7F00>'
    'ctgsen': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *, int *, int *, int *)" at 0x0000019E936D7F30>'
    'ctgsja': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, int *)" at 0x0000019E936D7F60>'
    'ctgsna': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_float_complex *, int *, int *, int *)" at 0x0000019E936D7F90>'
    'ctgsy2': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E936D7FC0>'
    'ctgsyl': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *, int *, int *)" at 0x0000019E936D9030>'
    'ctpcon': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E936D9060>'
    'ctpmqrt': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *)" at 0x0000019E936D9090>'
    'ctpqrt': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *)" at 0x0000019E936D90C0>'
    'ctpqrt2': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, int *)" at 0x0000019E936D90F0>'
    'ctprfb': None, # (!) real value is '<capsule object "void (char *, char *, char *, char *, int *, int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *)" at 0x0000019E936D9120>'
    'ctprfs': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E936D9150>'
    'ctptri': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_float_complex *, int *)" at 0x0000019E936D9180>'
    'ctptrs': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, int *)" at 0x0000019E936D91B0>'
    'ctpttf': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *)" at 0x0000019E936D91E0>'
    'ctpttr': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, int *)" at 0x0000019E936D9210>'
    'ctrcon': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E936D9240>'
    'ctrevc': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, int *, int *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E936D9270>'
    'ctrexc': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, int *, int *, int *)" at 0x0000019E936D92A0>'
    'ctrrfs': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E936D92D0>'
    'ctrsen': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *, int *)" at 0x0000019E936D9300>'
    'ctrsna': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E936D9330>'
    'ctrsyl': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E936D9360>'
    'ctrti2': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_float_complex *, int *, int *)" at 0x0000019E936D9390>'
    'ctrtri': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_float_complex *, int *, int *)" at 0x0000019E936D93C0>'
    'ctrtrs': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, int *)" at 0x0000019E936D93F0>'
    'ctrttf': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *)" at 0x0000019E936D9420>'
    'ctrttp': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *)" at 0x0000019E936D9450>'
    'ctzrzf': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, int *)" at 0x0000019E936D9480>'
    'cunbdb': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, int *)" at 0x0000019E936D94B0>'
    'cuncsd': None, # (!) real value is '<capsule object "void (char *, char *, char *, char *, char *, char *, int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *)" at 0x0000019E936D94E0>'
    'cung2l': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *)" at 0x0000019E936D9510>'
    'cung2r': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *)" at 0x0000019E936D9540>'
    'cungbr': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, int *)" at 0x0000019E936D9570>'
    'cunghr': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, int *)" at 0x0000019E936D95A0>'
    'cungl2': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *)" at 0x0000019E936D95D0>'
    'cunglq': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, int *)" at 0x0000019E936D9600>'
    'cungql': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, int *)" at 0x0000019E936D9630>'
    'cungqr': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, int *)" at 0x0000019E936D9660>'
    'cungr2': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *)" at 0x0000019E936D9690>'
    'cungrq': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, int *)" at 0x0000019E936D96C0>'
    'cungtr': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, int *)" at 0x0000019E936D96F0>'
    'cunm2l': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *)" at 0x0000019E936D9720>'
    'cunm2r': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *)" at 0x0000019E936D9750>'
    'cunmbr': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, int *)" at 0x0000019E936D9780>'
    'cunmhr': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, int *)" at 0x0000019E936D97B0>'
    'cunml2': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *)" at 0x0000019E936D97E0>'
    'cunmlq': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, int *)" at 0x0000019E936D9810>'
    'cunmql': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, int *)" at 0x0000019E936D9840>'
    'cunmqr': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, int *)" at 0x0000019E936D9870>'
    'cunmr2': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *)" at 0x0000019E936D98A0>'
    'cunmr3': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *)" at 0x0000019E936D98D0>'
    'cunmrq': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, int *)" at 0x0000019E936D9900>'
    'cunmrz': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, int *)" at 0x0000019E936D9930>'
    'cunmtr': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, int *)" at 0x0000019E936D9960>'
    'cupgtr': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *)" at 0x0000019E936D9990>'
    'cupmtr': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *)" at 0x0000019E936D99C0>'
    'dbbcsd': None, # (!) real value is '<capsule object "void (char *, char *, char *, char *, char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x0000019E936D99F0>'
    'dbdsdc': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x0000019E936D9A20>'
    'dbdsqr': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E936D9A50>'
    'ddisna': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E936D9A80>'
    'dgbbrd': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E936D9AB0>'
    'dgbcon': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x0000019E936D9AE0>'
    'dgbequ': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E936D9B10>'
    'dgbequb': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E936D9B40>'
    'dgbrfs': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x0000019E936D9B70>'
    'dgbsv': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x0000019E936D9BA0>'
    'dgbsvx': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, char *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x0000019E936D9BD0>'
    'dgbtf2': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *)" at 0x0000019E936D9C00>'
    'dgbtrf': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *)" at 0x0000019E936D9C30>'
    'dgbtrs': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x0000019E936D9C60>'
    'dgebak': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x0000019E936D9C90>'
    'dgebal': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E936D9CC0>'
    'dgebd2': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E936D9CF0>'
    'dgebrd': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x0000019E936D9D20>'
    'dgecon': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x0000019E936D9D50>'
    'dgeequ': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E936D9D80>'
    'dgeequb': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E936D9DB0>'
    'dgees': None, # (!) real value is '<capsule object "void (char *, char *, __pyx_t_5scipy_6linalg_13cython_lapack_dselect2 *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *)" at 0x0000019E936D9DE0>'
    'dgeesx': None, # (!) real value is '<capsule object "void (char *, char *, __pyx_t_5scipy_6linalg_13cython_lapack_dselect2 *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, int *, int *)" at 0x0000019E936D9E10>'
    'dgeev': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x0000019E936D9E40>'
    'dgeevx': None, # (!) real value is '<capsule object "void (char *, char *, char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *)" at 0x0000019E936D9E70>'
    'dgehd2': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E936D9EA0>'
    'dgehrd': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x0000019E936D9ED0>'
    'dgejsv': None, # (!) real value is '<capsule object "void (char *, char *, char *, char *, char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *)" at 0x0000019E936D9F00>'
    'dgelq2': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E936D9F30>'
    'dgelqf': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x0000019E936D9F60>'
    'dgels': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x0000019E936D9F90>'
    'dgelsd': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *)" at 0x0000019E936D9FC0>'
    'dgelss': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x0000019E936DA030>'
    'dgelsy': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x0000019E936DA060>'
    'dgemqrt': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E936DA090>'
    'dgeql2': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E936DA0C0>'
    'dgeqlf': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x0000019E936DA0F0>'
    'dgeqp3': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x0000019E936DA120>'
    'dgeqr2': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E936DA150>'
    'dgeqr2p': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E936DA180>'
    'dgeqrf': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x0000019E936DA1B0>'
    'dgeqrfp': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x0000019E936DA1E0>'
    'dgeqrt': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E936DA210>'
    'dgeqrt2': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x0000019E936DA240>'
    'dgeqrt3': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x0000019E936DA270>'
    'dgerfs': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x0000019E936DA2A0>'
    'dgerq2': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E936DA2D0>'
    'dgerqf': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x0000019E936DA300>'
    'dgesc2': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0x0000019E936DA330>'
    'dgesdd': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *)" at 0x0000019E936DA360>'
    'dgesv': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x0000019E936DA390>'
    'dgesvd': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x0000019E936DA3C0>'
    'dgesvj': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x0000019E936DA3F0>'
    'dgesvx': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, char *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x0000019E936DA420>'
    'dgetc2': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, int *)" at 0x0000019E936DA450>'
    'dgetf2': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *)" at 0x0000019E936DA480>'
    'dgetrf': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *)" at 0x0000019E936DA4B0>'
    'dgetri': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x0000019E936DA4E0>'
    'dgetrs': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x0000019E936DA510>'
    'dggbak': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x0000019E936DA540>'
    'dggbal': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E936DA570>'
    'dgges': None, # (!) real value is '<capsule object "void (char *, char *, char *, __pyx_t_5scipy_6linalg_13cython_lapack_dselect3 *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *)" at 0x0000019E936DA5A0>'
    'dggesx': None, # (!) real value is '<capsule object "void (char *, char *, char *, __pyx_t_5scipy_6linalg_13cython_lapack_dselect3 *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, int *, int *)" at 0x0000019E936DA5D0>'
    'dggev': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x0000019E936DA600>'
    'dggevx': None, # (!) real value is '<capsule object "void (char *, char *, char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, int *)" at 0x0000019E936DA630>'
    'dggglm': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x0000019E936DA660>'
    'dgghrd': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x0000019E936DA690>'
    'dgglse': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x0000019E936DA6C0>'
    'dggqrf': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x0000019E936DA6F0>'
    'dggrqf': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x0000019E936DA720>'
    'dgsvj0': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x0000019E936DA750>'
    'dgsvj1': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x0000019E936DA780>'
    'dgtcon': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x0000019E936DA7B0>'
    'dgtrfs': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x0000019E936DA7E0>'
    'dgtsv': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x0000019E936DA810>'
    'dgtsvx': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x0000019E936DA840>'
    'dgttrf': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x0000019E936DA870>'
    'dgttrs': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x0000019E936DA8A0>'
    'dgtts2': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E936DA8D0>'
    'dhgeqz': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x0000019E936DA900>'
    'dhsein': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *)" at 0x0000019E936DA930>'
    'dhseqr': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x0000019E936DA960>'
    'disnan': None, # (!) real value is '<capsule object "int (__pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0x0000019E936DA990>'
    'dlabad': None, # (!) real value is '<capsule object "void (__pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0x0000019E936DA9C0>'
    'dlabrd': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E936DA9F0>'
    'dlacn2': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x0000019E936DAA20>'
    'dlacon': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E936DAA50>'
    'dlacpy': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E936DAA80>'
    'dladiv': None, # (!) real value is '<capsule object "void (__pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0x0000019E936DAAB0>'
    'dlae2': None, # (!) real value is '<capsule object "void (__pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0x0000019E936DAAE0>'
    'dlaebz': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x0000019E936DAB10>'
    'dlaed0': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x0000019E936DAB40>'
    'dlaed1': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x0000019E936DAB70>'
    'dlaed2': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, int *, int *)" at 0x0000019E936DABA0>'
    'dlaed3': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E936DABD0>'
    'dlaed4': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E936DAC00>'
    'dlaed5': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0x0000019E936DAC30>'
    'dlaed6': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E936DAC60>'
    'dlaed7': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x0000019E936DAC90>'
    'dlaed8': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *)" at 0x0000019E936DACC0>'
    'dlaed9': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x0000019E936DACF0>'
    'dlaeda': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E936DAD20>'
    'dlaein': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E936DAD50>'
    'dlaev2': None, # (!) real value is '<capsule object "void (__pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0x0000019E936DAD80>'
    'dlaexc': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E936DADB0>'
    'dlag2': None, # (!) real value is '<capsule object "void (__pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0x0000019E936DADE0>'
    'dlag2s': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x0000019E936DAE10>'
    'dlags2': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0x0000019E936DAE40>'
    'dlagtf': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x0000019E936DAE70>'
    'dlagtm': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E936DAEA0>'
    'dlagts': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E936DAED0>'
    'dlagv2': None, # (!) real value is '<capsule object "void (__pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0x0000019E936DAF00>'
    'dlahqr': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x0000019E936DAF30>'
    'dlahr2': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E936DAF60>'
    'dlaic1': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0x0000019E936DAF90>'
    'dlaln2': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E936DAFC0>'
    'dlals0': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E936DC030>'
    'dlalsa': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x0000019E936DC060>'
    'dlalsd': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x0000019E936DC090>'
    'dlamch': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_13cython_lapack_d (char *)" at 0x0000019E936DC0C0>'
    'dlamrg': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *)" at 0x0000019E936DC0F0>'
    'dlaneg': None, # (!) real value is '<capsule object "int (int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E936DC120>'
    'dlangb': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_13cython_lapack_d (char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0x0000019E936DC150>'
    'dlange': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_13cython_lapack_d (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0x0000019E936DC180>'
    'dlangt': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_13cython_lapack_d (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0x0000019E936DC1B0>'
    'dlanhs': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_13cython_lapack_d (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0x0000019E936DC1E0>'
    'dlansb': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_13cython_lapack_d (char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0x0000019E936DC210>'
    'dlansf': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_13cython_lapack_d (char *, char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0x0000019E936DC240>'
    'dlansp': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_13cython_lapack_d (char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0x0000019E936DC270>'
    'dlanst': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_13cython_lapack_d (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0x0000019E936DC2A0>'
    'dlansy': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_13cython_lapack_d (char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0x0000019E936DC2D0>'
    'dlantb': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_13cython_lapack_d (char *, char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0x0000019E936DC300>'
    'dlantp': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_13cython_lapack_d (char *, char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0x0000019E936DC330>'
    'dlantr': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_13cython_lapack_d (char *, char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0x0000019E936DC360>'
    'dlanv2': None, # (!) real value is '<capsule object "void (__pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0x0000019E936DC390>'
    'dlapll': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0x0000019E936DC3C0>'
    'dlapmr': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x0000019E936DC3F0>'
    'dlapmt': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x0000019E936DC420>'
    'dlapy2': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_13cython_lapack_d (__pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0x0000019E936DC450>'
    'dlapy3': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_13cython_lapack_d (__pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0x0000019E936DC480>'
    'dlaqgb': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, char *)" at 0x0000019E936DC4B0>'
    'dlaqge': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, char *)" at 0x0000019E936DC4E0>'
    'dlaqp2': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0x0000019E936DC510>'
    'dlaqps': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E936DC540>'
    'dlaqr0': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x0000019E936DC570>'
    'dlaqr1': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0x0000019E936DC5A0>'
    'dlaqr2': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E936DC5D0>'
    'dlaqr3': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E936DC600>'
    'dlaqr4': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x0000019E936DC630>'
    'dlaqr5': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E936DC660>'
    'dlaqsb': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, char *)" at 0x0000019E936DC690>'
    'dlaqsp': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, char *)" at 0x0000019E936DC6C0>'
    'dlaqsy': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, char *)" at 0x0000019E936DC6F0>'
    'dlaqtr': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E936DC720>'
    'dlar1v': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0x0000019E936DC750>'
    'dlar2v': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E936DC780>'
    'dlarf': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0x0000019E936DC7B0>'
    'dlarfb': None, # (!) real value is '<capsule object "void (char *, char *, char *, char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E936DC7E0>'
    'dlarfg': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0x0000019E936DC810>'
    'dlarfgp': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0x0000019E936DC840>'
    'dlarft': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E936DC870>'
    'dlarfx': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0x0000019E936DC8A0>'
    'dlargv': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E936DC8D0>'
    'dlarnv': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0x0000019E936DC900>'
    'dlarra': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *)" at 0x0000019E936DC930>'
    'dlarrb': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x0000019E936DC960>'
    'dlarrc': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, int *)" at 0x0000019E936DC990>'
    'dlarrd': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x0000019E936DC9C0>'
    'dlarre': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x0000019E936DC9F0>'
    'dlarrf': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E936DCA20>'
    'dlarrj': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E936DCA50>'
    'dlarrk': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E936DCA80>'
    'dlarrr': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E936DCAB0>'
    'dlarrv': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x0000019E936DCAE0>'
    'dlartg': None, # (!) real value is '<capsule object "void (__pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0x0000019E936DCB10>'
    'dlartgp': None, # (!) real value is '<capsule object "void (__pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0x0000019E936DCB40>'
    'dlartgs': None, # (!) real value is '<capsule object "void (__pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0x0000019E936DCB70>'
    'dlartv': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E936DCBA0>'
    'dlaruv': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0x0000019E936DCBD0>'
    'dlarz': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0x0000019E936DCC00>'
    'dlarzb': None, # (!) real value is '<capsule object "void (char *, char *, char *, char *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E936DCC30>'
    'dlarzt': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E936DCC60>'
    'dlas2': None, # (!) real value is '<capsule object "void (__pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0x0000019E936DCC90>'
    'dlascl': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x0000019E936DCCC0>'
    'dlasd0': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E936DCCF0>'
    'dlasd1': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E936DCD20>'
    'dlasd2': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, int *, int *, int *, int *)" at 0x0000019E936DCD50>'
    'dlasd3': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E936DCD80>'
    'dlasd4': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E936DCDB0>'
    'dlasd5': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0x0000019E936DCDE0>'
    'dlasd6': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x0000019E936DCE10>'
    'dlasd7': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E936DCE40>'
    'dlasd8': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E936DCE70>'
    'dlasda': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x0000019E936DCEA0>'
    'dlasdq': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E936DCED0>'
    'dlasdt': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, int *, int *, int *)" at 0x0000019E936DCF00>'
    'dlaset': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E936DCF30>'
    'dlasq1': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E936DCF60>'
    'dlasq2': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E936DCF90>'
    'dlasq3': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0x0000019E936DCFC0>'
    'dlasq4': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0x0000019E936DE030>'
    'dlasq6': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0x0000019E936DE060>'
    'dlasr': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E936DE090>'
    'dlasrt': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E936DE0C0>'
    'dlassq': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0x0000019E936DE0F0>'
    'dlasv2': None, # (!) real value is '<capsule object "void (__pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0x0000019E936DE120>'
    'dlaswp': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, int *, int *)" at 0x0000019E936DE150>'
    'dlasy2': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E936DE180>'
    'dlasyf': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x0000019E936DE1B0>'
    'dlat2s': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x0000019E936DE1E0>'
    'dlatbs': None, # (!) real value is '<capsule object "void (char *, char *, char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E936DE210>'
    'dlatdf': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x0000019E936DE240>'
    'dlatps': None, # (!) real value is '<capsule object "void (char *, char *, char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E936DE270>'
    'dlatrd': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E936DE2A0>'
    'dlatrs': None, # (!) real value is '<capsule object "void (char *, char *, char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E936DE2D0>'
    'dlatrz': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0x0000019E936DE300>'
    'dlauu2': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x0000019E936DE330>'
    'dlauum': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x0000019E936DE360>'
    'dopgtr': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E936DE390>'
    'dopmtr': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E936DE3C0>'
    'dorbdb': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x0000019E936DE3F0>'
    'dorcsd': None, # (!) real value is '<capsule object "void (char *, char *, char *, char *, char *, char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *)" at 0x0000019E936DE420>'
    'dorg2l': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E936DE450>'
    'dorg2r': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E936DE480>'
    'dorgbr': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x0000019E936DE4B0>'
    'dorghr': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x0000019E936DE4E0>'
    'dorgl2': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E936DE510>'
    'dorglq': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x0000019E936DE540>'
    'dorgql': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x0000019E936DE570>'
    'dorgqr': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x0000019E936DE5A0>'
    'dorgr2': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E936DE5D0>'
    'dorgrq': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x0000019E936DE600>'
    'dorgtr': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x0000019E936DE630>'
    'dorm2l': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E936DE660>'
    'dorm2r': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E936DE690>'
    'dormbr': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x0000019E936DE6C0>'
    'dormhr': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x0000019E936DE6F0>'
    'dorml2': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E936DE720>'
    'dormlq': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x0000019E936DE750>'
    'dormql': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x0000019E936DE780>'
    'dormqr': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x0000019E936DE7B0>'
    'dormr2': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E936DE7E0>'
    'dormr3': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E936DE810>'
    'dormrq': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x0000019E936DE840>'
    'dormrz': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x0000019E936DE870>'
    'dormtr': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x0000019E936DE8A0>'
    'dpbcon': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x0000019E936DE8D0>'
    'dpbequ': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E936DE900>'
    'dpbrfs': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x0000019E936DE930>'
    'dpbstf': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x0000019E936DE960>'
    'dpbsv': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x0000019E936DE990>'
    'dpbsvx': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, char *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x0000019E936DE9C0>'
    'dpbtf2': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x0000019E936DE9F0>'
    'dpbtrf': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x0000019E936DEA20>'
    'dpbtrs': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x0000019E936DEA50>'
    'dpftrf': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E936DEA80>'
    'dpftri': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E936DEAB0>'
    'dpftrs': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x0000019E936DEAE0>'
    'dpocon': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x0000019E936DEB10>'
    'dpoequ': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E936DEB40>'
    'dpoequb': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E936DEB70>'
    'dporfs': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x0000019E936DEBA0>'
    'dposv': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x0000019E936DEBD0>'
    'dposvx': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, char *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x0000019E936DEC00>'
    'dpotf2': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x0000019E936DEC30>'
    'dpotrf': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x0000019E936DEC60>'
    'dpotri': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x0000019E936DEC90>'
    'dpotrs': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x0000019E936DECC0>'
    'dppcon': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x0000019E936DECF0>'
    'dppequ': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E936DED20>'
    'dpprfs': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x0000019E936DED50>'
    'dppsv': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x0000019E936DED80>'
    'dppsvx': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, char *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x0000019E936DEDB0>'
    'dpptrf': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E936DEDE0>'
    'dpptri': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E936DEE10>'
    'dpptrs': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x0000019E936DEE40>'
    'dpstf2': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E936DEE70>'
    'dpstrf': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E936DEEA0>'
    'dptcon': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E936DEED0>'
    'dpteqr': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E936DEF00>'
    'dptrfs': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E936DEF30>'
    'dptsv': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x0000019E936DEF60>'
    'dptsvx': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E936DEF90>'
    'dpttrf': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E936DEFC0>'
    'dpttrs': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x0000019E93720030>'
    'dptts2': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E93720060>'
    'drscl': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E93720090>'
    'dsbev': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E937200C0>'
    'dsbevd': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, int *)" at 0x0000019E937200F0>'
    'dsbevx': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *)" at 0x0000019E93720120>'
    'dsbgst': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E93720150>'
    'dsbgv': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E93720180>'
    'dsbgvd': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, int *)" at 0x0000019E937201B0>'
    'dsbgvx': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *)" at 0x0000019E937201E0>'
    'dsbtrd': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E93720210>'
    'dsfrk': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0x0000019E93720240>'
    'dsgesv': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x0000019E93720270>'
    'dspcon': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x0000019E937202A0>'
    'dspev': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E937202D0>'
    'dspevd': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, int *)" at 0x0000019E93720300>'
    'dspevx': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *)" at 0x0000019E93720330>'
    'dspgst': None, # (!) real value is '<capsule object "void (int *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E93720360>'
    'dspgv': None, # (!) real value is '<capsule object "void (int *, char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E93720390>'
    'dspgvd': None, # (!) real value is '<capsule object "void (int *, char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, int *)" at 0x0000019E937203C0>'
    'dspgvx': None, # (!) real value is '<capsule object "void (int *, char *, char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *)" at 0x0000019E937203F0>'
    'dsposv': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x0000019E93720420>'
    'dsprfs': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x0000019E93720450>'
    'dspsv': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x0000019E93720480>'
    'dspsvx': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x0000019E937204B0>'
    'dsptrd': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E937204E0>'
    'dsptrf': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x0000019E93720510>'
    'dsptri': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E93720540>'
    'dsptrs': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x0000019E93720570>'
    'dstebz': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x0000019E937205A0>'
    'dstedc': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, int *)" at 0x0000019E937205D0>'
    'dstegr': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, int *)" at 0x0000019E93720600>'
    'dstein': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *)" at 0x0000019E93720630>'
    'dstemr': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, int *)" at 0x0000019E93720660>'
    'dsteqr': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E93720690>'
    'dsterf': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E937206C0>'
    'dstev': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E937206F0>'
    'dstevd': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, int *)" at 0x0000019E93720720>'
    'dstevr': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, int *)" at 0x0000019E93720750>'
    'dstevx': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *)" at 0x0000019E93720780>'
    'dsycon': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x0000019E937207B0>'
    'dsyconv': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E937207E0>'
    'dsyequb': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E93720810>'
    'dsyev': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x0000019E93720840>'
    'dsyevd': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, int *)" at 0x0000019E93720870>'
    'dsyevr': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, int *)" at 0x0000019E937208A0>'
    'dsyevx': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, int *)" at 0x0000019E937208D0>'
    'dsygs2': None, # (!) real value is '<capsule object "void (int *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x0000019E93720900>'
    'dsygst': None, # (!) real value is '<capsule object "void (int *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x0000019E93720930>'
    'dsygv': None, # (!) real value is '<capsule object "void (int *, char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x0000019E93720960>'
    'dsygvd': None, # (!) real value is '<capsule object "void (int *, char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, int *)" at 0x0000019E93720990>'
    'dsygvx': None, # (!) real value is '<capsule object "void (int *, char *, char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, int *)" at 0x0000019E937209C0>'
    'dsyrfs': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x0000019E937209F0>'
    'dsysv': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x0000019E93720A20>'
    'dsysvx': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *)" at 0x0000019E93720A50>'
    'dsyswapr': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *)" at 0x0000019E93720A80>'
    'dsytd2': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E93720AB0>'
    'dsytf2': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *)" at 0x0000019E93720AE0>'
    'dsytrd': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x0000019E93720B10>'
    'dsytrf': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x0000019E93720B40>'
    'dsytri': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E93720B70>'
    'dsytri2': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x0000019E93720BA0>'
    'dsytri2x': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x0000019E93720BD0>'
    'dsytrs': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x0000019E93720C00>'
    'dsytrs2': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E93720C30>'
    'dtbcon': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x0000019E93720C60>'
    'dtbrfs': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x0000019E93720C90>'
    'dtbtrs': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x0000019E93720CC0>'
    'dtfsm': None, # (!) real value is '<capsule object "void (char *, char *, char *, char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E93720CF0>'
    'dtftri': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E93720D20>'
    'dtfttp': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E93720D50>'
    'dtfttr': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x0000019E93720D80>'
    'dtgevc': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E93720DB0>'
    'dtgex2': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x0000019E93720DE0>'
    'dtgexc': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x0000019E93720E10>'
    'dtgsen': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, int *)" at 0x0000019E93720E40>'
    'dtgsja': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x0000019E93720E70>'
    'dtgsna': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *)" at 0x0000019E93720EA0>'
    'dtgsy2': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *)" at 0x0000019E93720ED0>'
    'dtgsyl': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *)" at 0x0000019E93720F00>'
    'dtpcon': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x0000019E93720F30>'
    'dtpmqrt': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E93720F60>'
    'dtpqrt': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E93720F90>'
    'dtpqrt2': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x0000019E93720FC0>'
    'dtprfb': None, # (!) real value is '<capsule object "void (char *, char *, char *, char *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E93722030>'
    'dtprfs': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x0000019E93722060>'
    'dtptri': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E93722090>'
    'dtptrs': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x0000019E937220C0>'
    'dtpttf': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E937220F0>'
    'dtpttr': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x0000019E93722120>'
    'dtrcon': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x0000019E93722150>'
    'dtrevc': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E93722180>'
    'dtrexc': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E937221B0>'
    'dtrrfs': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x0000019E937221E0>'
    'dtrsen': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, int *)" at 0x0000019E93722210>'
    'dtrsna': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *)" at 0x0000019E93722240>'
    'dtrsyl': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E93722270>'
    'dtrti2': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x0000019E937222A0>'
    'dtrtri': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x0000019E937222D0>'
    'dtrtrs': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x0000019E93722300>'
    'dtrttf': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E93722330>'
    'dtrttp': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E93722360>'
    'dtzrzf': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x0000019E93722390>'
    'dzsum1': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_13cython_lapack_d (int *, __pyx_t_double_complex *, int *)" at 0x0000019E937223C0>'
    'icmax1': None, # (!) real value is '<capsule object "int (int *, __pyx_t_float_complex *, int *)" at 0x0000019E937223F0>'
    'ieeeck': None, # (!) real value is '<capsule object "int (int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0x0000019E93722420>'
    'ilaclc': None, # (!) real value is '<capsule object "int (int *, int *, __pyx_t_float_complex *, int *)" at 0x0000019E93722450>'
    'ilaclr': None, # (!) real value is '<capsule object "int (int *, int *, __pyx_t_float_complex *, int *)" at 0x0000019E93722480>'
    'iladiag': None, # (!) real value is '<capsule object "int (char *)" at 0x0000019E937224B0>'
    'iladlc': None, # (!) real value is '<capsule object "int (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E937224E0>'
    'iladlr': None, # (!) real value is '<capsule object "int (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E93722510>'
    'ilaprec': None, # (!) real value is '<capsule object "int (char *)" at 0x0000019E93722540>'
    'ilaslc': None, # (!) real value is '<capsule object "int (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E93722570>'
    'ilaslr': None, # (!) real value is '<capsule object "int (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E937225A0>'
    'ilatrans': None, # (!) real value is '<capsule object "int (char *)" at 0x0000019E937225D0>'
    'ilauplo': None, # (!) real value is '<capsule object "int (char *)" at 0x0000019E93722600>'
    'ilaver': None, # (!) real value is '<capsule object "void (int *, int *, int *)" at 0x0000019E93722630>'
    'ilazlc': None, # (!) real value is '<capsule object "int (int *, int *, __pyx_t_double_complex *, int *)" at 0x0000019E93722660>'
    'ilazlr': None, # (!) real value is '<capsule object "int (int *, int *, __pyx_t_double_complex *, int *)" at 0x0000019E93722690>'
    'izmax1': None, # (!) real value is '<capsule object "int (int *, __pyx_t_double_complex *, int *)" at 0x0000019E937226C0>'
    'sbbcsd': None, # (!) real value is '<capsule object "void (char *, char *, char *, char *, char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x0000019E937226F0>'
    'sbdsdc': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x0000019E93722720>'
    'sbdsqr': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E93722750>'
    'scsum1': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_13cython_lapack_s (int *, __pyx_t_float_complex *, int *)" at 0x0000019E93722780>'
    'sdisna': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E937227B0>'
    'sgbbrd': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E937227E0>'
    'sgbcon': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x0000019E93722810>'
    'sgbequ': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E93722840>'
    'sgbequb': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E93722870>'
    'sgbrfs': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x0000019E937228A0>'
    'sgbsv': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x0000019E937228D0>'
    'sgbsvx': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, char *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x0000019E93722900>'
    'sgbtf2': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *)" at 0x0000019E93722930>'
    'sgbtrf': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *)" at 0x0000019E93722960>'
    'sgbtrs': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x0000019E93722990>'
    'sgebak': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x0000019E937229C0>'
    'sgebal': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E937229F0>'
    'sgebd2': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E93722A20>'
    'sgebrd': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x0000019E93722A50>'
    'sgecon': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x0000019E93722A80>'
    'sgeequ': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E93722AB0>'
    'sgeequb': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E93722AE0>'
    'sgees': None, # (!) real value is '<capsule object "void (char *, char *, __pyx_t_5scipy_6linalg_13cython_lapack_sselect2 *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *)" at 0x0000019E93722B10>'
    'sgeesx': None, # (!) real value is '<capsule object "void (char *, char *, __pyx_t_5scipy_6linalg_13cython_lapack_sselect2 *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, int *, int *)" at 0x0000019E93722B40>'
    'sgeev': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x0000019E93722B70>'
    'sgeevx': None, # (!) real value is '<capsule object "void (char *, char *, char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *)" at 0x0000019E93722BA0>'
    'sgehd2': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E93722BD0>'
    'sgehrd': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x0000019E93722C00>'
    'sgejsv': None, # (!) real value is '<capsule object "void (char *, char *, char *, char *, char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *)" at 0x0000019E93722C30>'
    'sgelq2': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E93722C60>'
    'sgelqf': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x0000019E93722C90>'
    'sgels': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x0000019E93722CC0>'
    'sgelsd': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *)" at 0x0000019E93722CF0>'
    'sgelss': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x0000019E93722D20>'
    'sgelsy': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x0000019E93722D50>'
    'sgemqrt': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E93722D80>'
    'sgeql2': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E93722DB0>'
    'sgeqlf': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x0000019E93722DE0>'
    'sgeqp3': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x0000019E93722E10>'
    'sgeqr2': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E93722E40>'
    'sgeqr2p': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E93722E70>'
    'sgeqrf': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x0000019E93722EA0>'
    'sgeqrfp': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x0000019E93722ED0>'
    'sgeqrt': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E93722F00>'
    'sgeqrt2': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x0000019E93722F30>'
    'sgeqrt3': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x0000019E93722F60>'
    'sgerfs': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x0000019E93722F90>'
    'sgerq2': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E93722FC0>'
    'sgerqf': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x0000019E93724030>'
    'sgesc2': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0x0000019E93724060>'
    'sgesdd': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *)" at 0x0000019E93724090>'
    'sgesv': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x0000019E937240C0>'
    'sgesvd': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x0000019E937240F0>'
    'sgesvj': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x0000019E93724120>'
    'sgesvx': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, char *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x0000019E93724150>'
    'sgetc2': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, int *)" at 0x0000019E93724180>'
    'sgetf2': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *)" at 0x0000019E937241B0>'
    'sgetrf': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *)" at 0x0000019E937241E0>'
    'sgetri': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x0000019E93724210>'
    'sgetrs': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x0000019E93724240>'
    'sggbak': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x0000019E93724270>'
    'sggbal': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E937242A0>'
    'sgges': None, # (!) real value is '<capsule object "void (char *, char *, char *, __pyx_t_5scipy_6linalg_13cython_lapack_sselect3 *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *)" at 0x0000019E937242D0>'
    'sggesx': None, # (!) real value is '<capsule object "void (char *, char *, char *, __pyx_t_5scipy_6linalg_13cython_lapack_sselect3 *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, int *, int *)" at 0x0000019E93724300>'
    'sggev': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x0000019E93724330>'
    'sggevx': None, # (!) real value is '<capsule object "void (char *, char *, char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, int *)" at 0x0000019E93724360>'
    'sggglm': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x0000019E93724390>'
    'sgghrd': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x0000019E937243C0>'
    'sgglse': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x0000019E937243F0>'
    'sggqrf': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x0000019E93724420>'
    'sggrqf': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x0000019E93724450>'
    'sgsvj0': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x0000019E93724480>'
    'sgsvj1': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x0000019E937244B0>'
    'sgtcon': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x0000019E937244E0>'
    'sgtrfs': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x0000019E93724510>'
    'sgtsv': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x0000019E93724540>'
    'sgtsvx': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x0000019E93724570>'
    'sgttrf': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x0000019E937245A0>'
    'sgttrs': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x0000019E937245D0>'
    'sgtts2': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E93724600>'
    'shgeqz': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x0000019E93724630>'
    'shsein': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *)" at 0x0000019E93724660>'
    'shseqr': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x0000019E93724690>'
    'slabad': None, # (!) real value is '<capsule object "void (__pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0x0000019E937246C0>'
    'slabrd': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E937246F0>'
    'slacn2': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x0000019E93724720>'
    'slacon': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E93724750>'
    'slacpy': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E93724780>'
    'sladiv': None, # (!) real value is '<capsule object "void (__pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0x0000019E937247B0>'
    'slae2': None, # (!) real value is '<capsule object "void (__pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0x0000019E937247E0>'
    'slaebz': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x0000019E93724810>'
    'slaed0': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x0000019E93724840>'
    'slaed1': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x0000019E93724870>'
    'slaed2': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, int *, int *)" at 0x0000019E937248A0>'
    'slaed3': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E937248D0>'
    'slaed4': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E93724900>'
    'slaed5': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0x0000019E93724930>'
    'slaed6': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E93724960>'
    'slaed7': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x0000019E93724990>'
    'slaed8': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *)" at 0x0000019E937249C0>'
    'slaed9': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x0000019E937249F0>'
    'slaeda': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E93724A20>'
    'slaein': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E93724A50>'
    'slaev2': None, # (!) real value is '<capsule object "void (__pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0x0000019E93724A80>'
    'slaexc': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E93724AB0>'
    'slag2': None, # (!) real value is '<capsule object "void (__pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0x0000019E93724AE0>'
    'slag2d': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x0000019E93724B10>'
    'slags2': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0x0000019E93724B40>'
    'slagtf': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x0000019E93724B70>'
    'slagtm': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E93724BA0>'
    'slagts': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E93724BD0>'
    'slagv2': None, # (!) real value is '<capsule object "void (__pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0x0000019E93724C00>'
    'slahqr': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x0000019E93724C30>'
    'slahr2': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E93724C60>'
    'slaic1': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0x0000019E93724C90>'
    'slaln2': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E93724CC0>'
    'slals0': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E93724CF0>'
    'slalsa': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x0000019E93724D20>'
    'slalsd': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x0000019E93724D50>'
    'slamch': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_13cython_lapack_s (char *)" at 0x0000019E93724D80>'
    'slamrg': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *)" at 0x0000019E93724DB0>'
    'slangb': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_13cython_lapack_s (char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0x0000019E93724DE0>'
    'slange': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_13cython_lapack_s (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0x0000019E93724E10>'
    'slangt': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_13cython_lapack_s (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0x0000019E93724E40>'
    'slanhs': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_13cython_lapack_s (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0x0000019E93724E70>'
    'slansb': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_13cython_lapack_s (char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0x0000019E93724EA0>'
    'slansf': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_13cython_lapack_s (char *, char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0x0000019E93724ED0>'
    'slansp': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_13cython_lapack_s (char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0x0000019E93724F00>'
    'slanst': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_13cython_lapack_s (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0x0000019E93724F30>'
    'slansy': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_13cython_lapack_s (char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0x0000019E93724F60>'
    'slantb': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_13cython_lapack_s (char *, char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0x0000019E93724F90>'
    'slantp': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_13cython_lapack_s (char *, char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0x0000019E93724FC0>'
    'slantr': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_13cython_lapack_s (char *, char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0x0000019E93726030>'
    'slanv2': None, # (!) real value is '<capsule object "void (__pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0x0000019E93726060>'
    'slapll': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0x0000019E93726090>'
    'slapmr': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x0000019E937260C0>'
    'slapmt': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x0000019E937260F0>'
    'slapy2': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_13cython_lapack_s (__pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0x0000019E93726120>'
    'slapy3': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_13cython_lapack_s (__pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0x0000019E93726150>'
    'slaqgb': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, char *)" at 0x0000019E93726180>'
    'slaqge': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, char *)" at 0x0000019E937261B0>'
    'slaqp2': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0x0000019E937261E0>'
    'slaqps': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E93726210>'
    'slaqr0': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x0000019E93726240>'
    'slaqr1': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0x0000019E93726270>'
    'slaqr2': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E937262A0>'
    'slaqr3': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E937262D0>'
    'slaqr4': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x0000019E93726300>'
    'slaqr5': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E93726330>'
    'slaqsb': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, char *)" at 0x0000019E93726360>'
    'slaqsp': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, char *)" at 0x0000019E93726390>'
    'slaqsy': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, char *)" at 0x0000019E937263C0>'
    'slaqtr': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E937263F0>'
    'slar1v': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0x0000019E93726420>'
    'slar2v': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E93726450>'
    'slarf': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0x0000019E93726480>'
    'slarfb': None, # (!) real value is '<capsule object "void (char *, char *, char *, char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E937264B0>'
    'slarfg': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0x0000019E937264E0>'
    'slarfgp': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0x0000019E93726510>'
    'slarft': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E93726540>'
    'slarfx': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0x0000019E93726570>'
    'slargv': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E937265A0>'
    'slarnv': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0x0000019E937265D0>'
    'slarra': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *)" at 0x0000019E93726600>'
    'slarrb': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x0000019E93726630>'
    'slarrc': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, int *)" at 0x0000019E93726660>'
    'slarrd': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x0000019E93726690>'
    'slarre': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x0000019E937266C0>'
    'slarrf': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E937266F0>'
    'slarrj': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E93726720>'
    'slarrk': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E93726750>'
    'slarrr': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E93726780>'
    'slarrv': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x0000019E937267B0>'
    'slartg': None, # (!) real value is '<capsule object "void (__pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0x0000019E937267E0>'
    'slartgp': None, # (!) real value is '<capsule object "void (__pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0x0000019E93726810>'
    'slartgs': None, # (!) real value is '<capsule object "void (__pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0x0000019E93726840>'
    'slartv': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E93726870>'
    'slaruv': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0x0000019E937268A0>'
    'slarz': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0x0000019E937268D0>'
    'slarzb': None, # (!) real value is '<capsule object "void (char *, char *, char *, char *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E93726900>'
    'slarzt': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E93726930>'
    'slas2': None, # (!) real value is '<capsule object "void (__pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0x0000019E93726960>'
    'slascl': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x0000019E93726990>'
    'slasd0': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E937269C0>'
    'slasd1': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E937269F0>'
    'slasd2': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, int *, int *, int *, int *)" at 0x0000019E93726A20>'
    'slasd3': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E93726A50>'
    'slasd4': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E93726A80>'
    'slasd5': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0x0000019E93726AB0>'
    'slasd6': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x0000019E93726AE0>'
    'slasd7': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E93726B10>'
    'slasd8': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E93726B40>'
    'slasda': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x0000019E93726B70>'
    'slasdq': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E93726BA0>'
    'slasdt': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, int *, int *, int *)" at 0x0000019E93726BD0>'
    'slaset': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E93726C00>'
    'slasq1': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E93726C30>'
    'slasq2': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E93726C60>'
    'slasq3': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0x0000019E93726C90>'
    'slasq4': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0x0000019E93726CC0>'
    'slasq6': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0x0000019E93726CF0>'
    'slasr': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E93726D20>'
    'slasrt': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E93726D50>'
    'slassq': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0x0000019E93726D80>'
    'slasv2': None, # (!) real value is '<capsule object "void (__pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0x0000019E93726DB0>'
    'slaswp': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, int *, int *)" at 0x0000019E93726DE0>'
    'slasy2': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E93726E10>'
    'slasyf': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x0000019E93726E40>'
    'slatbs': None, # (!) real value is '<capsule object "void (char *, char *, char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E93726E70>'
    'slatdf': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x0000019E93726EA0>'
    'slatps': None, # (!) real value is '<capsule object "void (char *, char *, char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E93726ED0>'
    'slatrd': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E93726F00>'
    'slatrs': None, # (!) real value is '<capsule object "void (char *, char *, char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E93726F30>'
    'slatrz': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0x0000019E93726F60>'
    'slauu2': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x0000019E93726F90>'
    'slauum': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x0000019E93726FC0>'
    'sopgtr': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E93728030>'
    'sopmtr': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E93728060>'
    'sorbdb': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x0000019E93728090>'
    'sorcsd': None, # (!) real value is '<capsule object "void (char *, char *, char *, char *, char *, char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *)" at 0x0000019E937280C0>'
    'sorg2l': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E937280F0>'
    'sorg2r': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E93728120>'
    'sorgbr': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x0000019E93728150>'
    'sorghr': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x0000019E93728180>'
    'sorgl2': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E937281B0>'
    'sorglq': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x0000019E937281E0>'
    'sorgql': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x0000019E93728210>'
    'sorgqr': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x0000019E93728240>'
    'sorgr2': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E93728270>'
    'sorgrq': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x0000019E937282A0>'
    'sorgtr': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x0000019E937282D0>'
    'sorm2l': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E93728300>'
    'sorm2r': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E93728330>'
    'sormbr': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x0000019E93728360>'
    'sormhr': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x0000019E93728390>'
    'sorml2': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E937283C0>'
    'sormlq': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x0000019E937283F0>'
    'sormql': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x0000019E93728420>'
    'sormqr': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x0000019E93728450>'
    'sormr2': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E93728480>'
    'sormr3': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E937284B0>'
    'sormrq': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x0000019E937284E0>'
    'sormrz': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x0000019E93728510>'
    'sormtr': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x0000019E93728540>'
    'spbcon': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x0000019E93728570>'
    'spbequ': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E937285A0>'
    'spbrfs': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x0000019E937285D0>'
    'spbstf': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x0000019E93728600>'
    'spbsv': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x0000019E93728630>'
    'spbsvx': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, char *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x0000019E93728660>'
    'spbtf2': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x0000019E93728690>'
    'spbtrf': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x0000019E937286C0>'
    'spbtrs': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x0000019E937286F0>'
    'spftrf': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E93728720>'
    'spftri': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E93728750>'
    'spftrs': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x0000019E93728780>'
    'spocon': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x0000019E937287B0>'
    'spoequ': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E937287E0>'
    'spoequb': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E93728810>'
    'sporfs': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x0000019E93728840>'
    'sposv': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x0000019E93728870>'
    'sposvx': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, char *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x0000019E937288A0>'
    'spotf2': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x0000019E937288D0>'
    'spotrf': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x0000019E93728900>'
    'spotri': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x0000019E93728930>'
    'spotrs': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x0000019E93728960>'
    'sppcon': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x0000019E93728990>'
    'sppequ': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E937289C0>'
    'spprfs': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x0000019E937289F0>'
    'sppsv': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x0000019E93728A20>'
    'sppsvx': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, char *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x0000019E93728A50>'
    'spptrf': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E93728A80>'
    'spptri': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E93728AB0>'
    'spptrs': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x0000019E93728AE0>'
    'spstf2': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E93728B10>'
    'spstrf': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E93728B40>'
    'sptcon': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E93728B70>'
    'spteqr': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E93728BA0>'
    'sptrfs': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E93728BD0>'
    'sptsv': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x0000019E93728C00>'
    'sptsvx': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E93728C30>'
    'spttrf': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E93728C60>'
    'spttrs': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x0000019E93728C90>'
    'sptts2': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E93728CC0>'
    'srscl': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E93728CF0>'
    'ssbev': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E93728D20>'
    'ssbevd': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, int *)" at 0x0000019E93728D50>'
    'ssbevx': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *)" at 0x0000019E93728D80>'
    'ssbgst': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E93728DB0>'
    'ssbgv': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E93728DE0>'
    'ssbgvd': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, int *)" at 0x0000019E93728E10>'
    'ssbgvx': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *)" at 0x0000019E93728E40>'
    'ssbtrd': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E93728E70>'
    'ssfrk': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0x0000019E93728EA0>'
    'sspcon': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x0000019E93728ED0>'
    'sspev': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E93728F00>'
    'sspevd': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, int *)" at 0x0000019E93728F30>'
    'sspevx': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *)" at 0x0000019E93728F60>'
    'sspgst': None, # (!) real value is '<capsule object "void (int *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E93728F90>'
    'sspgv': None, # (!) real value is '<capsule object "void (int *, char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E93728FC0>'
    'sspgvd': None, # (!) real value is '<capsule object "void (int *, char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, int *)" at 0x0000019E9372A030>'
    'sspgvx': None, # (!) real value is '<capsule object "void (int *, char *, char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *)" at 0x0000019E9372A060>'
    'ssprfs': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x0000019E9372A090>'
    'sspsv': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x0000019E9372A0C0>'
    'sspsvx': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x0000019E9372A0F0>'
    'ssptrd': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E9372A120>'
    'ssptrf': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x0000019E9372A150>'
    'ssptri': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E9372A180>'
    'ssptrs': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x0000019E9372A1B0>'
    'sstebz': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x0000019E9372A1E0>'
    'sstedc': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, int *)" at 0x0000019E9372A210>'
    'sstegr': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, int *)" at 0x0000019E9372A240>'
    'sstein': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *)" at 0x0000019E9372A270>'
    'sstemr': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, int *)" at 0x0000019E9372A2A0>'
    'ssteqr': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E9372A2D0>'
    'ssterf': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E9372A300>'
    'sstev': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E9372A330>'
    'sstevd': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, int *)" at 0x0000019E9372A360>'
    'sstevr': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, int *)" at 0x0000019E9372A390>'
    'sstevx': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *)" at 0x0000019E9372A3C0>'
    'ssycon': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x0000019E9372A3F0>'
    'ssyconv': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E9372A420>'
    'ssyequb': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E9372A450>'
    'ssyev': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x0000019E9372A480>'
    'ssyevd': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, int *)" at 0x0000019E9372A4B0>'
    'ssyevr': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, int *)" at 0x0000019E9372A4E0>'
    'ssyevx': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, int *)" at 0x0000019E9372A510>'
    'ssygs2': None, # (!) real value is '<capsule object "void (int *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x0000019E9372A540>'
    'ssygst': None, # (!) real value is '<capsule object "void (int *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x0000019E9372A570>'
    'ssygv': None, # (!) real value is '<capsule object "void (int *, char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x0000019E9372A5A0>'
    'ssygvd': None, # (!) real value is '<capsule object "void (int *, char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, int *)" at 0x0000019E9372A5D0>'
    'ssygvx': None, # (!) real value is '<capsule object "void (int *, char *, char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, int *)" at 0x0000019E9372A600>'
    'ssyrfs': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x0000019E9372A630>'
    'ssysv': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x0000019E9372A660>'
    'ssysvx': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *)" at 0x0000019E9372A690>'
    'ssyswapr': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *)" at 0x0000019E9372A6C0>'
    'ssytd2': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E9372A6F0>'
    'ssytf2': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *)" at 0x0000019E9372A720>'
    'ssytrd': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x0000019E9372A750>'
    'ssytrf': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x0000019E9372A780>'
    'ssytri': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E9372A7B0>'
    'ssytri2': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x0000019E9372A7E0>'
    'ssytri2x': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x0000019E9372A810>'
    'ssytrs': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x0000019E9372A840>'
    'ssytrs2': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E9372A870>'
    'stbcon': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x0000019E9372A8A0>'
    'stbrfs': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x0000019E9372A8D0>'
    'stbtrs': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x0000019E9372A900>'
    'stfsm': None, # (!) real value is '<capsule object "void (char *, char *, char *, char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E9372A930>'
    'stftri': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E9372A960>'
    'stfttp': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E9372A990>'
    'stfttr': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x0000019E9372A9C0>'
    'stgevc': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E9372A9F0>'
    'stgex2': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x0000019E9372AA20>'
    'stgexc': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x0000019E9372AA50>'
    'stgsen': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, int *)" at 0x0000019E9372AA80>'
    'stgsja': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x0000019E9372AAB0>'
    'stgsna': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *)" at 0x0000019E9372AAE0>'
    'stgsy2': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *)" at 0x0000019E9372AB10>'
    'stgsyl': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *)" at 0x0000019E9372AB40>'
    'stpcon': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x0000019E9372AB70>'
    'stpmqrt': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E9372ABA0>'
    'stpqrt': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E9372ABD0>'
    'stpqrt2': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x0000019E9372AC00>'
    'stprfb': None, # (!) real value is '<capsule object "void (char *, char *, char *, char *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E9372AC30>'
    'stprfs': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x0000019E9372AC60>'
    'stptri': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E9372AC90>'
    'stptrs': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x0000019E9372ACC0>'
    'stpttf': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E9372ACF0>'
    'stpttr': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x0000019E9372AD20>'
    'strcon': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x0000019E9372AD50>'
    'strevc': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E9372AD80>'
    'strexc': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E9372ADB0>'
    'strrfs': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x0000019E9372ADE0>'
    'strsen': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, int *)" at 0x0000019E9372AE10>'
    'strsna': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *)" at 0x0000019E9372AE40>'
    'strsyl': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E9372AE70>'
    'strti2': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x0000019E9372AEA0>'
    'strtri': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x0000019E9372AED0>'
    'strtrs': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x0000019E9372AF00>'
    'strttf': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E9372AF30>'
    'strttp': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x0000019E9372AF60>'
    'stzrzf': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x0000019E9372AF90>'
    'xerbla_array': None, # (!) real value is '<capsule object "void (char *, int *, int *)" at 0x0000019E9372AFC0>'
    'zbbcsd': None, # (!) real value is '<capsule object "void (char *, char *, char *, char *, char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x0000019E9372C030>'
    'zbdsqr': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E9372C060>'
    'zcgesv': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_double_complex *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x0000019E9372C090>'
    'zcposv': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x0000019E9372C0C0>'
    'zdrscl': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *)" at 0x0000019E9372C0F0>'
    'zgbbrd': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E9372C120>'
    'zgbcon': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, __pyx_t_double_complex *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E9372C150>'
    'zgbequ': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E9372C180>'
    'zgbequb': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E9372C1B0>'
    'zgbrfs': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E9372C1E0>'
    'zgbsv': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, __pyx_t_double_complex *, int *, int *, __pyx_t_double_complex *, int *, int *)" at 0x0000019E9372C210>'
    'zgbsvx': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, int *, char *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E9372C240>'
    'zgbtf2': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, __pyx_t_double_complex *, int *, int *, int *)" at 0x0000019E9372C270>'
    'zgbtrf': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, __pyx_t_double_complex *, int *, int *, int *)" at 0x0000019E9372C2A0>'
    'zgbtrs': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, int *, __pyx_t_double_complex *, int *, int *, __pyx_t_double_complex *, int *, int *)" at 0x0000019E9372C2D0>'
    'zgebak': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_double_complex *, int *, int *)" at 0x0000019E9372C300>'
    'zgebal': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_double_complex *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E9372C330>'
    'zgebd2': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *)" at 0x0000019E9372C360>'
    'zgebrd': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, int *)" at 0x0000019E9372C390>'
    'zgecon': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E9372C3C0>'
    'zgeequ': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E9372C3F0>'
    'zgeequb': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E9372C420>'
    'zgees': None, # (!) real value is '<capsule object "void (char *, char *, __pyx_t_5scipy_6linalg_13cython_lapack_zselect1 *, int *, __pyx_t_double_complex *, int *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x0000019E9372C450>'
    'zgeesx': None, # (!) real value is '<capsule object "void (char *, char *, __pyx_t_5scipy_6linalg_13cython_lapack_zselect1 *, char *, int *, __pyx_t_double_complex *, int *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x0000019E9372C480>'
    'zgeev': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E9372C4B0>'
    'zgeevx': None, # (!) real value is '<capsule object "void (char *, char *, char *, char *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E9372C4E0>'
    'zgehd2': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *)" at 0x0000019E9372C510>'
    'zgehrd': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, int *)" at 0x0000019E9372C540>'
    'zgelq2': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *)" at 0x0000019E9372C570>'
    'zgelqf': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, int *)" at 0x0000019E9372C5A0>'
    'zgels': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, int *)" at 0x0000019E9372C5D0>'
    'zgelsd': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x0000019E9372C600>'
    'zgelss': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E9372C630>'
    'zgelsy': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E9372C660>'
    'zgemqrt': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *)" at 0x0000019E9372C690>'
    'zgeql2': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *)" at 0x0000019E9372C6C0>'
    'zgeqlf': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, int *)" at 0x0000019E9372C6F0>'
    'zgeqp3': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_double_complex *, int *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E9372C720>'
    'zgeqr2': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *)" at 0x0000019E9372C750>'
    'zgeqr2p': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *)" at 0x0000019E9372C780>'
    'zgeqrf': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, int *)" at 0x0000019E9372C7B0>'
    'zgeqrfp': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, int *)" at 0x0000019E9372C7E0>'
    'zgeqrt': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *)" at 0x0000019E9372C810>'
    'zgeqrt2': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, int *)" at 0x0000019E9372C840>'
    'zgeqrt3': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, int *)" at 0x0000019E9372C870>'
    'zgerfs': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E9372C8A0>'
    'zgerq2': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *)" at 0x0000019E9372C8D0>'
    'zgerqf': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, int *)" at 0x0000019E9372C900>'
    'zgesc2': None, # (!) real value is '<capsule object "void (int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0x0000019E9372C930>'
    'zgesdd': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x0000019E9372C960>'
    'zgesv': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_double_complex *, int *, int *, __pyx_t_double_complex *, int *, int *)" at 0x0000019E9372C990>'
    'zgesvd': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E9372C9C0>'
    'zgesvx': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, int *, char *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E9372C9F0>'
    'zgetc2': None, # (!) real value is '<capsule object "void (int *, __pyx_t_double_complex *, int *, int *, int *, int *)" at 0x0000019E9372CA20>'
    'zgetf2': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_double_complex *, int *, int *, int *)" at 0x0000019E9372CA50>'
    'zgetrf': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_double_complex *, int *, int *, int *)" at 0x0000019E9372CA80>'
    'zgetri': None, # (!) real value is '<capsule object "void (int *, __pyx_t_double_complex *, int *, int *, __pyx_t_double_complex *, int *, int *)" at 0x0000019E9372CAB0>'
    'zgetrs': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_double_complex *, int *, int *, __pyx_t_double_complex *, int *, int *)" at 0x0000019E9372CAE0>'
    'zggbak': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_double_complex *, int *, int *)" at 0x0000019E9372CB10>'
    'zggbal': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E9372CB40>'
    'zgges': None, # (!) real value is '<capsule object "void (char *, char *, char *, __pyx_t_5scipy_6linalg_13cython_lapack_zselect2 *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x0000019E9372CB70>'
    'zggesx': None, # (!) real value is '<capsule object "void (char *, char *, char *, __pyx_t_5scipy_6linalg_13cython_lapack_zselect2 *, char *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, int *)" at 0x0000019E9372CBA0>'
    'zggev': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E9372CBD0>'
    'zggevx': None, # (!) real value is '<capsule object "void (char *, char *, char *, char *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *)" at 0x0000019E9372CC00>'
    'zggglm': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, int *)" at 0x0000019E9372CC30>'
    'zgghrd': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, int *)" at 0x0000019E9372CC60>'
    'zgglse': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, int *)" at 0x0000019E9372CC90>'
    'zggqrf': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, int *)" at 0x0000019E9372CCC0>'
    'zggrqf': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, int *)" at 0x0000019E9372CCF0>'
    'zgtcon': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *)" at 0x0000019E9372CD20>'
    'zgtrfs': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E9372CD50>'
    'zgtsv': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, int *)" at 0x0000019E9372CD80>'
    'zgtsvx': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E9372CDB0>'
    'zgttrf': None, # (!) real value is '<capsule object "void (int *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, int *)" at 0x0000019E9372CDE0>'
    'zgttrs': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, int *)" at 0x0000019E9372CE10>'
    'zgtts2': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *)" at 0x0000019E9372CE40>'
    'zhbev': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E9372CE70>'
    'zhbevd': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, int *)" at 0x0000019E9372CEA0>'
    'zhbevx': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *)" at 0x0000019E9372CED0>'
    'zhbgst': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E9372CF00>'
    'zhbgv': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E9372CF30>'
    'zhbgvd': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, int *)" at 0x0000019E9372CF60>'
    'zhbgvx': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *)" at 0x0000019E9372CF90>'
    'zhbtrd': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *)" at 0x0000019E9372CFC0>'
    'zhecon': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_double_complex *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *)" at 0x0000019E9372D030>'
    'zheequb': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *)" at 0x0000019E9372D060>'
    'zheev': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E9372D090>'
    'zheevd': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, int *)" at 0x0000019E9372D0C0>'
    'zheevr': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, int *)" at 0x0000019E9372D0F0>'
    'zheevx': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *)" at 0x0000019E9372D120>'
    'zhegs2': None, # (!) real value is '<capsule object "void (int *, char *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, int *)" at 0x0000019E9372D150>'
    'zhegst': None, # (!) real value is '<capsule object "void (int *, char *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, int *)" at 0x0000019E9372D180>'
    'zhegv': None, # (!) real value is '<capsule object "void (int *, char *, char *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E9372D1B0>'
    'zhegvd': None, # (!) real value is '<capsule object "void (int *, char *, char *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, int *)" at 0x0000019E9372D1E0>'
    'zhegvx': None, # (!) real value is '<capsule object "void (int *, char *, char *, char *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *)" at 0x0000019E9372D210>'
    'zherfs': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E9372D240>'
    'zhesv': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_double_complex *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, int *)" at 0x0000019E9372D270>'
    'zhesvx': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E9372D2A0>'
    'zheswapr': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_double_complex *, int *, int *, int *)" at 0x0000019E9372D2D0>'
    'zhetd2': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *)" at 0x0000019E9372D300>'
    'zhetf2': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_double_complex *, int *, int *, int *)" at 0x0000019E9372D330>'
    'zhetrd': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, int *)" at 0x0000019E9372D360>'
    'zhetrf': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_double_complex *, int *, int *, __pyx_t_double_complex *, int *, int *)" at 0x0000019E9372D390>'
    'zhetri': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_double_complex *, int *, int *, __pyx_t_double_complex *, int *)" at 0x0000019E9372D3C0>'
    'zhetri2': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_double_complex *, int *, int *, __pyx_t_double_complex *, int *, int *)" at 0x0000019E9372D3F0>'
    'zhetri2x': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_double_complex *, int *, int *, __pyx_t_double_complex *, int *, int *)" at 0x0000019E9372D420>'
    'zhetrs': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_double_complex *, int *, int *, __pyx_t_double_complex *, int *, int *)" at 0x0000019E9372D450>'
    'zhetrs2': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_double_complex *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *)" at 0x0000019E9372D480>'
    'zhfrk': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *)" at 0x0000019E9372D4B0>'
    'zhgeqz': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E9372D4E0>'
    'zhpcon': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *)" at 0x0000019E9372D510>'
    'zhpev': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E9372D540>'
    'zhpevd': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, int *)" at 0x0000019E9372D570>'
    'zhpevx': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *)" at 0x0000019E9372D5A0>'
    'zhpgst': None, # (!) real value is '<capsule object "void (int *, char *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *)" at 0x0000019E9372D5D0>'
    'zhpgv': None, # (!) real value is '<capsule object "void (int *, char *, char *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E9372D600>'
    'zhpgvd': None, # (!) real value is '<capsule object "void (int *, char *, char *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, int *)" at 0x0000019E9372D630>'
    'zhpgvx': None, # (!) real value is '<capsule object "void (int *, char *, char *, char *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *)" at 0x0000019E9372D660>'
    'zhprfs': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E9372D690>'
    'zhpsv': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, int *)" at 0x0000019E9372D6C0>'
    'zhpsvx': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E9372D6F0>'
    'zhptrd': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *)" at 0x0000019E9372D720>'
    'zhptrf': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_double_complex *, int *, int *)" at 0x0000019E9372D750>'
    'zhptri': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *)" at 0x0000019E9372D780>'
    'zhptrs': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, int *)" at 0x0000019E9372D7B0>'
    'zhsein': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, int *, int *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *)" at 0x0000019E9372D7E0>'
    'zhseqr': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, int *)" at 0x0000019E9372D810>'
    'zlabrd': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *)" at 0x0000019E9372D840>'
    'zlacgv': None, # (!) real value is '<capsule object "void (int *, __pyx_t_double_complex *, int *)" at 0x0000019E9372D870>'
    'zlacn2': None, # (!) real value is '<capsule object "void (int *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x0000019E9372D8A0>'
    'zlacon': None, # (!) real value is '<capsule object "void (int *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E9372D8D0>'
    'zlacp2': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_double_complex *, int *)" at 0x0000019E9372D900>'
    'zlacpy': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *)" at 0x0000019E9372D930>'
    'zlacrm': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0x0000019E9372D960>'
    'zlacrt': None, # (!) real value is '<capsule object "void (int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *)" at 0x0000019E9372D990>'
    'zladiv': None, # (!) real value is '<capsule object "__pyx_t_double_complex (__pyx_t_double_complex *, __pyx_t_double_complex *)" at 0x0000019E9372D9C0>'
    'zlaed0': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x0000019E9372D9F0>'
    'zlaed7': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x0000019E9372DA20>'
    'zlaed8': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E9372DA50>'
    'zlaein': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E9372DA80>'
    'zlaesy': None, # (!) real value is '<capsule object "void (__pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_double_complex *)" at 0x0000019E9372DAB0>'
    'zlaev2': None, # (!) real value is '<capsule object "void (__pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *)" at 0x0000019E9372DAE0>'
    'zlag2c': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_double_complex *, int *, __pyx_t_float_complex *, int *, int *)" at 0x0000019E9372DB10>'
    'zlags2': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *)" at 0x0000019E9372DB40>'
    'zlagtm': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *)" at 0x0000019E9372DB70>'
    'zlahef': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, __pyx_t_double_complex *, int *, int *, __pyx_t_double_complex *, int *, int *)" at 0x0000019E9372DBA0>'
    'zlahqr': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, int *, __pyx_t_double_complex *, int *, int *)" at 0x0000019E9372DBD0>'
    'zlahr2': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *)" at 0x0000019E9372DC00>'
    'zlaic1': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, __pyx_t_double_complex *)" at 0x0000019E9372DC30>'
    'zlals0': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E9372DC60>'
    'zlalsa': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x0000019E9372DC90>'
    'zlalsd': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x0000019E9372DCC0>'
    'zlangb': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_13cython_lapack_d (char *, int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0x0000019E9372DCF0>'
    'zlange': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_13cython_lapack_d (char *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0x0000019E9372DD20>'
    'zlangt': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_13cython_lapack_d (char *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_double_complex *)" at 0x0000019E9372DD50>'
    'zlanhb': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_13cython_lapack_d (char *, char *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0x0000019E9372DD80>'
    'zlanhe': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_13cython_lapack_d (char *, char *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0x0000019E9372DDB0>'
    'zlanhf': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_13cython_lapack_d (char *, char *, char *, int *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0x0000019E9372DDE0>'
    'zlanhp': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_13cython_lapack_d (char *, char *, int *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0x0000019E9372DE10>'
    'zlanhs': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_13cython_lapack_d (char *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0x0000019E9372DE40>'
    'zlanht': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_13cython_lapack_d (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *)" at 0x0000019E9372DE70>'
    'zlansb': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_13cython_lapack_d (char *, char *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0x0000019E9372DEA0>'
    'zlansp': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_13cython_lapack_d (char *, char *, int *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0x0000019E9372DED0>'
    'zlansy': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_13cython_lapack_d (char *, char *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0x0000019E9372DF00>'
    'zlantb': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_13cython_lapack_d (char *, char *, char *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0x0000019E9372DF30>'
    'zlantp': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_13cython_lapack_d (char *, char *, char *, int *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0x0000019E9372DF60>'
    'zlantr': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_13cython_lapack_d (char *, char *, char *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0x0000019E9372DF90>'
    'zlapll': None, # (!) real value is '<capsule object "void (int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0x0000019E9372DFC0>'
    'zlapmr': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_double_complex *, int *, int *)" at 0x0000019E9372F030>'
    'zlapmt': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_double_complex *, int *, int *)" at 0x0000019E9372F060>'
    'zlaqgb': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, char *)" at 0x0000019E9372F090>'
    'zlaqge': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, char *)" at 0x0000019E9372F0C0>'
    'zlaqhb': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, char *)" at 0x0000019E9372F0F0>'
    'zlaqhe': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, char *)" at 0x0000019E9372F120>'
    'zlaqhp': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, char *)" at 0x0000019E9372F150>'
    'zlaqp2': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_double_complex *, int *, int *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *)" at 0x0000019E9372F180>'
    'zlaqps': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, int *, __pyx_t_double_complex *, int *, int *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *)" at 0x0000019E9372F1B0>'
    'zlaqr0': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, int *)" at 0x0000019E9372F1E0>'
    'zlaqr1': None, # (!) real value is '<capsule object "void (int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_double_complex *)" at 0x0000019E9372F210>'
    'zlaqr2': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, int *, int *, __pyx_t_double_complex *, int *, int *, int *, __pyx_t_double_complex *, int *, int *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, int *, __pyx_t_double_complex *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *)" at 0x0000019E9372F240>'
    'zlaqr3': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, int *, int *, __pyx_t_double_complex *, int *, int *, int *, __pyx_t_double_complex *, int *, int *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, int *, __pyx_t_double_complex *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *)" at 0x0000019E9372F270>'
    'zlaqr4': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, int *)" at 0x0000019E9372F2A0>'
    'zlaqr5': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, int *, int *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, int *, __pyx_t_double_complex *, int *, int *, __pyx_t_double_complex *, int *)" at 0x0000019E9372F2D0>'
    'zlaqsb': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, char *)" at 0x0000019E9372F300>'
    'zlaqsp': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, char *)" at 0x0000019E9372F330>'
    'zlaqsy': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, char *)" at 0x0000019E9372F360>'
    'zlar1v': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0x0000019E9372F390>'
    'zlar2v': None, # (!) real value is '<capsule object "void (int *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *)" at 0x0000019E9372F3C0>'
    'zlarcm': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0x0000019E9372F3F0>'
    'zlarf': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *)" at 0x0000019E9372F420>'
    'zlarfb': None, # (!) real value is '<capsule object "void (char *, char *, char *, char *, int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *)" at 0x0000019E9372F450>'
    'zlarfg': None, # (!) real value is '<capsule object "void (int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *)" at 0x0000019E9372F480>'
    'zlarfgp': None, # (!) real value is '<capsule object "void (int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *)" at 0x0000019E9372F4B0>'
    'zlarft': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *)" at 0x0000019E9372F4E0>'
    'zlarfx': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *)" at 0x0000019E9372F510>'
    'zlargv': None, # (!) real value is '<capsule object "void (int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E9372F540>'
    'zlarnv': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_double_complex *)" at 0x0000019E9372F570>'
    'zlarrv': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x0000019E9372F5A0>'
    'zlartg': None, # (!) real value is '<capsule object "void (__pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, __pyx_t_double_complex *)" at 0x0000019E9372F5D0>'
    'zlartv': None, # (!) real value is '<capsule object "void (int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *)" at 0x0000019E9372F600>'
    'zlarz': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *)" at 0x0000019E9372F630>'
    'zlarzb': None, # (!) real value is '<capsule object "void (char *, char *, char *, char *, int *, int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *)" at 0x0000019E9372F660>'
    'zlarzt': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *)" at 0x0000019E9372F690>'
    'zlascl': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_double_complex *, int *, int *)" at 0x0000019E9372F6C0>'
    'zlaset': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *)" at 0x0000019E9372F6F0>'
    'zlasr': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *)" at 0x0000019E9372F720>'
    'zlassq': None, # (!) real value is '<capsule object "void (int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0x0000019E9372F750>'
    'zlaswp': None, # (!) real value is '<capsule object "void (int *, __pyx_t_double_complex *, int *, int *, int *, int *, int *)" at 0x0000019E9372F780>'
    'zlasyf': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, __pyx_t_double_complex *, int *, int *, __pyx_t_double_complex *, int *, int *)" at 0x0000019E9372F7B0>'
    'zlat2c': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_double_complex *, int *, __pyx_t_float_complex *, int *, int *)" at 0x0000019E9372F7E0>'
    'zlatbs': None, # (!) real value is '<capsule object "void (char *, char *, char *, char *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E9372F810>'
    'zlatdf': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x0000019E9372F840>'
    'zlatps': None, # (!) real value is '<capsule object "void (char *, char *, char *, char *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E9372F870>'
    'zlatrd': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *)" at 0x0000019E9372F8A0>'
    'zlatrs': None, # (!) real value is '<capsule object "void (char *, char *, char *, char *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E9372F8D0>'
    'zlatrz': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *)" at 0x0000019E9372F900>'
    'zlauu2': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_double_complex *, int *, int *)" at 0x0000019E9372F930>'
    'zlauum': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_double_complex *, int *, int *)" at 0x0000019E9372F960>'
    'zpbcon': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E9372F990>'
    'zpbequ': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E9372F9C0>'
    'zpbrfs': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E9372F9F0>'
    'zpbstf': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_double_complex *, int *, int *)" at 0x0000019E9372FA20>'
    'zpbsv': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, int *)" at 0x0000019E9372FA50>'
    'zpbsvx': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, char *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E9372FA80>'
    'zpbtf2': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_double_complex *, int *, int *)" at 0x0000019E9372FAB0>'
    'zpbtrf': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_double_complex *, int *, int *)" at 0x0000019E9372FAE0>'
    'zpbtrs': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, int *)" at 0x0000019E9372FB10>'
    'zpftrf': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_double_complex *, int *)" at 0x0000019E9372FB40>'
    'zpftri': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_double_complex *, int *)" at 0x0000019E9372FB70>'
    'zpftrs': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, int *)" at 0x0000019E9372FBA0>'
    'zpocon': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E9372FBD0>'
    'zpoequ': None, # (!) real value is '<capsule object "void (int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E9372FC00>'
    'zpoequb': None, # (!) real value is '<capsule object "void (int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E9372FC30>'
    'zporfs': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E9372FC60>'
    'zposv': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, int *)" at 0x0000019E9372FC90>'
    'zposvx': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, char *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E9372FCC0>'
    'zpotf2': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_double_complex *, int *, int *)" at 0x0000019E9372FCF0>'
    'zpotrf': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_double_complex *, int *, int *)" at 0x0000019E9372FD20>'
    'zpotri': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_double_complex *, int *, int *)" at 0x0000019E9372FD50>'
    'zpotrs': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, int *)" at 0x0000019E9372FD80>'
    'zppcon': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E9372FDB0>'
    'zppequ': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E9372FDE0>'
    'zpprfs': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E9372FE10>'
    'zppsv': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, int *)" at 0x0000019E9372FE40>'
    'zppsvx': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, char *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E9372FE70>'
    'zpptrf': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_double_complex *, int *)" at 0x0000019E9372FEA0>'
    'zpptri': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_double_complex *, int *)" at 0x0000019E9372FED0>'
    'zpptrs': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, int *)" at 0x0000019E9372FF00>'
    'zpstf2': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_double_complex *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E9372FF30>'
    'zpstrf': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_double_complex *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E9372FF60>'
    'zptcon': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E9372FF90>'
    'zpteqr': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E9372FFC0>'
    'zptrfs': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E93731030>'
    'zptsv': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, int *)" at 0x0000019E93731060>'
    'zptsvx': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E93731090>'
    'zpttrf': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *)" at 0x0000019E937310C0>'
    'zpttrs': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, int *)" at 0x0000019E937310F0>'
    'zptts2': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *)" at 0x0000019E93731120>'
    'zrot': None, # (!) real value is '<capsule object "void (int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *)" at 0x0000019E93731150>'
    'zspcon': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *)" at 0x0000019E93731180>'
    'zspmv': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *)" at 0x0000019E937311B0>'
    'zspr': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *)" at 0x0000019E937311E0>'
    'zsprfs': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E93731210>'
    'zspsv': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, int *)" at 0x0000019E93731240>'
    'zspsvx': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E93731270>'
    'zsptrf': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_double_complex *, int *, int *)" at 0x0000019E937312A0>'
    'zsptri': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *)" at 0x0000019E937312D0>'
    'zsptrs': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, int *)" at 0x0000019E93731300>'
    'zstedc': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, int *)" at 0x0000019E93731330>'
    'zstegr': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, int *)" at 0x0000019E93731360>'
    'zstein': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *)" at 0x0000019E93731390>'
    'zstemr': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, int *)" at 0x0000019E937313C0>'
    'zsteqr': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E937313F0>'
    'zsycon': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_double_complex *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *)" at 0x0000019E93731420>'
    'zsyconv': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_double_complex *, int *, int *, __pyx_t_double_complex *, int *)" at 0x0000019E93731450>'
    'zsyequb': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *)" at 0x0000019E93731480>'
    'zsymv': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *)" at 0x0000019E937314B0>'
    'zsyr': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *)" at 0x0000019E937314E0>'
    'zsyrfs': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E93731510>'
    'zsysv': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_double_complex *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, int *)" at 0x0000019E93731540>'
    'zsysvx': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E93731570>'
    'zsyswapr': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_double_complex *, int *, int *, int *)" at 0x0000019E937315A0>'
    'zsytf2': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_double_complex *, int *, int *, int *)" at 0x0000019E937315D0>'
    'zsytrf': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_double_complex *, int *, int *, __pyx_t_double_complex *, int *, int *)" at 0x0000019E93731600>'
    'zsytri': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_double_complex *, int *, int *, __pyx_t_double_complex *, int *)" at 0x0000019E93731630>'
    'zsytri2': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_double_complex *, int *, int *, __pyx_t_double_complex *, int *, int *)" at 0x0000019E93731660>'
    'zsytri2x': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_double_complex *, int *, int *, __pyx_t_double_complex *, int *, int *)" at 0x0000019E93731690>'
    'zsytrs': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_double_complex *, int *, int *, __pyx_t_double_complex *, int *, int *)" at 0x0000019E937316C0>'
    'zsytrs2': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_double_complex *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *)" at 0x0000019E937316F0>'
    'ztbcon': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E93731720>'
    'ztbrfs': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E93731750>'
    'ztbtrs': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, int *)" at 0x0000019E93731780>'
    'ztfsm': None, # (!) real value is '<capsule object "void (char *, char *, char *, char *, char *, int *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *)" at 0x0000019E937317B0>'
    'ztftri': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, __pyx_t_double_complex *, int *)" at 0x0000019E937317E0>'
    'ztfttp': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *)" at 0x0000019E93731810>'
    'ztfttr': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, int *)" at 0x0000019E93731840>'
    'ztgevc': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, int *, int *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E93731870>'
    'ztgex2': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, int *, int *)" at 0x0000019E937318A0>'
    'ztgexc': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, int *, int *, int *)" at 0x0000019E937318D0>'
    'ztgsen': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *, int *, int *, int *)" at 0x0000019E93731900>'
    'ztgsja': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, int *)" at 0x0000019E93731930>'
    'ztgsna': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_double_complex *, int *, int *, int *)" at 0x0000019E93731960>'
    'ztgsy2': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E93731990>'
    'ztgsyl': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *, int *, int *)" at 0x0000019E937319C0>'
    'ztpcon': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E937319F0>'
    'ztpmqrt': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *)" at 0x0000019E93731A20>'
    'ztpqrt': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *)" at 0x0000019E93731A50>'
    'ztpqrt2': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, int *)" at 0x0000019E93731A80>'
    'ztprfb': None, # (!) real value is '<capsule object "void (char *, char *, char *, char *, int *, int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *)" at 0x0000019E93731AB0>'
    'ztprfs': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E93731AE0>'
    'ztptri': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_double_complex *, int *)" at 0x0000019E93731B10>'
    'ztptrs': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, int *)" at 0x0000019E93731B40>'
    'ztpttf': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *)" at 0x0000019E93731B70>'
    'ztpttr': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, int *)" at 0x0000019E93731BA0>'
    'ztrcon': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E93731BD0>'
    'ztrevc': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, int *, int *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E93731C00>'
    'ztrexc': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, int *, int *, int *)" at 0x0000019E93731C30>'
    'ztrrfs': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E93731C60>'
    'ztrsen': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *, int *)" at 0x0000019E93731C90>'
    'ztrsna': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E93731CC0>'
    'ztrsyl': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x0000019E93731CF0>'
    'ztrti2': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_double_complex *, int *, int *)" at 0x0000019E93731D20>'
    'ztrtri': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_double_complex *, int *, int *)" at 0x0000019E93731D50>'
    'ztrtrs': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, int *)" at 0x0000019E93731D80>'
    'ztrttf': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *)" at 0x0000019E93731DB0>'
    'ztrttp': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *)" at 0x0000019E93731DE0>'
    'ztzrzf': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, int *)" at 0x0000019E93731E10>'
    'zunbdb': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, int *)" at 0x0000019E93731E40>'
    'zuncsd': None, # (!) real value is '<capsule object "void (char *, char *, char *, char *, char *, char *, int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *)" at 0x0000019E93731E70>'
    'zung2l': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *)" at 0x0000019E93731EA0>'
    'zung2r': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *)" at 0x0000019E93731ED0>'
    'zungbr': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, int *)" at 0x0000019E93731F00>'
    'zunghr': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, int *)" at 0x0000019E93731F30>'
    'zungl2': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *)" at 0x0000019E93731F60>'
    'zunglq': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, int *)" at 0x0000019E93731F90>'
    'zungql': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, int *)" at 0x0000019E93731FC0>'
    'zungqr': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, int *)" at 0x0000019E93733030>'
    'zungr2': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *)" at 0x0000019E93733060>'
    'zungrq': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, int *)" at 0x0000019E93733090>'
    'zungtr': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, int *)" at 0x0000019E937330C0>'
    'zunm2l': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *)" at 0x0000019E937330F0>'
    'zunm2r': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *)" at 0x0000019E93733120>'
    'zunmbr': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, int *)" at 0x0000019E93733150>'
    'zunmhr': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, int *)" at 0x0000019E93733180>'
    'zunml2': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *)" at 0x0000019E937331B0>'
    'zunmlq': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, int *)" at 0x0000019E937331E0>'
    'zunmql': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, int *)" at 0x0000019E93733210>'
    'zunmqr': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, int *)" at 0x0000019E93733240>'
    'zunmr2': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *)" at 0x0000019E93733270>'
    'zunmr3': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *)" at 0x0000019E937332A0>'
    'zunmrq': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, int *)" at 0x0000019E937332D0>'
    'zunmrz': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, int *)" at 0x0000019E93733300>'
    'zunmtr': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, int *)" at 0x0000019E93733330>'
    'zupgtr': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *)" at 0x0000019E93733360>'
    'zupmtr': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *)" at 0x0000019E93733390>'
}

__spec__ = None # (!) real value is "ModuleSpec(name='scipy.linalg.cython_lapack', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x0000019E936CBF28>, origin='C:\\\\Users\\\\Doly\\\\Anaconda3\\\\lib\\\\site-packages\\\\scipy\\\\linalg\\\\cython_lapack.cp37-win_amd64.pyd')"

__test__ = {}

