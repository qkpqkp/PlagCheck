# encoding: utf-8
# module gevent.libuv._corecffi.lib
# from C:\Users\Doly\Anaconda3\lib\site-packages\gevent\__abstract_linkable.cp37-win_amd64.pyd
# by generator 1.147
# no doc

# imports
from _cffi_backend import (_uv_close_callback, gevent_noop, python_callback, 
    python_check_callback, python_handle_error, python_prepare_callback, 
    python_queue_callback, python_sigchld_callback, python_stop, 
    python_timer0_callback)


# Variables with simple values

UV_ASYNC = 1
UV_CHANGE = 2
UV_CHECK = 2
UV_DISCONNECT = 4
UV_EBUSY = -4082
UV_FILE = 17

UV_FS_EVENT = 3

UV_FS_EVENT_RECURSIVE = 4
UV_FS_EVENT_STAT = 2

UV_FS_EVENT_WATCH_ENTRY = 1

UV_FS_POLL = 4

UV_HANDLE = 5

UV_HANDLE_TYPE_MAX = 18

UV_IDLE = 6

UV_NAMED_PIPE = 7

UV_POLL = 8
UV_PREPARE = 9
UV_PRIORITIZED = 8
UV_PROCESS = 10
UV_READABLE = 1
UV_RENAME = 1

UV_RUN_DEFAULT = 0
UV_RUN_NOWAIT = 2
UV_RUN_ONCE = 1

UV_SIGNAL = 16
UV_STREAM = 11
UV_TCP = 12
UV_TIMER = 13
UV_TTY = 14
UV_UDP = 15

UV_UNKNOWN_HANDLE = 0

UV_VERSION_MAJOR = 1
UV_VERSION_MINOR = 24
UV_VERSION_PATCH = 0

UV_WRITABLE = 2

# functions

def gevent_close_all_handles(struct_uv_loop_s, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void gevent_close_all_handles(struct uv_loop_s *);
    
    CFFI C function from gevent.libuv._corecffi.lib
    """
    pass

def gevent_uv_walk_callback_close(struct_uv_handle_s, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void gevent_uv_walk_callback_close(struct uv_handle_s *, void *);
    
    CFFI C function from gevent.libuv._corecffi.lib
    """
    pass

def gevent_zero_check(struct_uv_check_s, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void gevent_zero_check(struct uv_check_s *);
    
    CFFI C function from gevent.libuv._corecffi.lib
    """
    pass

def gevent_zero_loop(struct_uv_loop_s, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void gevent_zero_loop(struct uv_loop_s *);
    
    CFFI C function from gevent.libuv._corecffi.lib
    """
    pass

def gevent_zero_prepare(struct_uv_prepare_s, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void gevent_zero_prepare(struct uv_prepare_s *);
    
    CFFI C function from gevent.libuv._corecffi.lib
    """
    pass

def gevent_zero_timer(struct_uv_timer_s, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void gevent_zero_timer(struct uv_timer_s *);
    
    CFFI C function from gevent.libuv._corecffi.lib
    """
    pass

def memset(void, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void *memset(void *, int, size_t);
    
    CFFI C function from gevent.libuv._corecffi.lib
    """
    pass

def uv_async_init(struct_uv_loop_s, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int uv_async_init(struct uv_loop_s *, struct uv_async_s *, void(*)(struct uv_async_s *));
    
    CFFI C function from gevent.libuv._corecffi.lib
    """
    pass

def uv_async_send(struct_uv_async_s, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int uv_async_send(struct uv_async_s *);
    
    CFFI C function from gevent.libuv._corecffi.lib
    """
    pass

def uv_backend_fd(struct_uv_loop_s, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int uv_backend_fd(struct uv_loop_s *);
    
    CFFI C function from gevent.libuv._corecffi.lib
    """
    pass

def uv_backend_timeout(struct_uv_loop_s, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    uint64_t uv_backend_timeout(struct uv_loop_s *);
    
    CFFI C function from gevent.libuv._corecffi.lib
    """
    pass

def uv_check_init(struct_uv_loop_s, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int uv_check_init(struct uv_loop_s *, struct uv_check_s *);
    
    CFFI C function from gevent.libuv._corecffi.lib
    """
    pass

def uv_check_start(struct_uv_check_s, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int uv_check_start(struct uv_check_s *, void(*)(struct uv_check_s *));
    
    CFFI C function from gevent.libuv._corecffi.lib
    """
    pass

def uv_check_stop(struct_uv_check_s, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int uv_check_stop(struct uv_check_s *);
    
    CFFI C function from gevent.libuv._corecffi.lib
    """
    pass

def uv_close(void, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void uv_close(void *, void(*)(struct uv_handle_s *));
    
    CFFI C function from gevent.libuv._corecffi.lib
    """
    pass

def uv_default_loop(): # real signature unknown; restored from __doc__
    """
    struct uv_loop_s *uv_default_loop();
    
    CFFI C function from gevent.libuv._corecffi.lib
    """
    pass

def uv_err_name(p_int): # real signature unknown; restored from __doc__
    """
    char *uv_err_name(int);
    
    CFFI C function from gevent.libuv._corecffi.lib
    """
    pass

def uv_fs_event_getpath(struct_uv_fs_event_s, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int uv_fs_event_getpath(struct uv_fs_event_s *, char *, size_t *);
    
    CFFI C function from gevent.libuv._corecffi.lib
    """
    pass

def uv_fs_event_init(struct_uv_loop_s, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int uv_fs_event_init(struct uv_loop_s *, struct uv_fs_event_s *);
    
    CFFI C function from gevent.libuv._corecffi.lib
    """
    pass

def uv_fs_event_start(struct_uv_fs_event_s, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int uv_fs_event_start(struct uv_fs_event_s *, void(*)(struct uv_fs_event_s *, char *, int, int), char *, unsigned int);
    
    CFFI C function from gevent.libuv._corecffi.lib
    """
    pass

def uv_fs_event_stop(struct_uv_fs_event_s, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int uv_fs_event_stop(struct uv_fs_event_s *);
    
    CFFI C function from gevent.libuv._corecffi.lib
    """
    pass

def uv_fs_poll_init(void, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int uv_fs_poll_init(void *, void *);
    
    CFFI C function from gevent.libuv._corecffi.lib
    """
    pass

def uv_fs_poll_start(void, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int uv_fs_poll_start(void *, void(*)(struct uv_fs_poll_s *, int, uv_stat_t *, uv_stat_t *), char *, unsigned int);
    
    CFFI C function from gevent.libuv._corecffi.lib
    """
    pass

def uv_fs_poll_stop(void, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int uv_fs_poll_stop(void *);
    
    CFFI C function from gevent.libuv._corecffi.lib
    """
    pass

def uv_handle_size(uv_handle_type): # real signature unknown; restored from __doc__
    """
    size_t uv_handle_size(uv_handle_type);
    
    CFFI C function from gevent.libuv._corecffi.lib
    """
    pass

def uv_handle_type_name(uv_handle_type): # real signature unknown; restored from __doc__
    """
    char *uv_handle_type_name(uv_handle_type);
    
    CFFI C function from gevent.libuv._corecffi.lib
    """
    pass

def uv_has_ref(void, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int uv_has_ref(void *);
    
    CFFI C function from gevent.libuv._corecffi.lib
    """
    pass

def uv_idle_init(struct_uv_loop_s, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int uv_idle_init(struct uv_loop_s *, struct uv_idle_s *);
    
    CFFI C function from gevent.libuv._corecffi.lib
    """
    pass

def uv_idle_start(struct_uv_idle_s, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int uv_idle_start(struct uv_idle_s *, void(*)(struct uv_idle_s *));
    
    CFFI C function from gevent.libuv._corecffi.lib
    """
    pass

def uv_idle_stop(struct_uv_idle_s, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int uv_idle_stop(struct uv_idle_s *);
    
    CFFI C function from gevent.libuv._corecffi.lib
    """
    pass

def uv_is_active(void, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int uv_is_active(void *);
    
    CFFI C function from gevent.libuv._corecffi.lib
    """
    pass

def uv_is_closing(void, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int uv_is_closing(void *);
    
    CFFI C function from gevent.libuv._corecffi.lib
    """
    pass

def uv_loop_alive(struct_uv_loop_s, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int uv_loop_alive(struct uv_loop_s *);
    
    CFFI C function from gevent.libuv._corecffi.lib
    """
    pass

def uv_loop_close(struct_uv_loop_s, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int uv_loop_close(struct uv_loop_s *);
    
    CFFI C function from gevent.libuv._corecffi.lib
    """
    pass

def uv_loop_fork(struct_uv_loop_s, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int uv_loop_fork(struct uv_loop_s *);
    
    CFFI C function from gevent.libuv._corecffi.lib
    """
    pass

def uv_loop_init(struct_uv_loop_s, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int uv_loop_init(struct uv_loop_s *);
    
    CFFI C function from gevent.libuv._corecffi.lib
    """
    pass

def uv_loop_new(): # real signature unknown; restored from __doc__
    """
    struct uv_loop_s *uv_loop_new();
    
    CFFI C function from gevent.libuv._corecffi.lib
    """
    pass

def uv_now(struct_uv_loop_s, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    uint64_t uv_now(struct uv_loop_s *);
    
    CFFI C function from gevent.libuv._corecffi.lib
    """
    pass

def uv_poll_init(struct_uv_loop_s, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int uv_poll_init(struct uv_loop_s *, struct uv_poll_s *, int);
    
    CFFI C function from gevent.libuv._corecffi.lib
    """
    pass

def uv_poll_init_socket(struct_uv_loop_s, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int uv_poll_init_socket(struct uv_loop_s *, struct uv_poll_s *, intptr_t);
    
    CFFI C function from gevent.libuv._corecffi.lib
    """
    pass

def uv_poll_start(struct_uv_poll_s, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int uv_poll_start(struct uv_poll_s *, int, void(*)(struct uv_poll_s *, int, int));
    
    CFFI C function from gevent.libuv._corecffi.lib
    """
    pass

def uv_poll_stop(struct_uv_poll_s, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int uv_poll_stop(struct uv_poll_s *);
    
    CFFI C function from gevent.libuv._corecffi.lib
    """
    pass

def uv_prepare_init(struct_uv_loop_s, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int uv_prepare_init(struct uv_loop_s *, struct uv_prepare_s *);
    
    CFFI C function from gevent.libuv._corecffi.lib
    """
    pass

def uv_prepare_start(struct_uv_prepare_s, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int uv_prepare_start(struct uv_prepare_s *, void(*)(struct uv_prepare_s *));
    
    CFFI C function from gevent.libuv._corecffi.lib
    """
    pass

def uv_prepare_stop(struct_uv_prepare_s, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int uv_prepare_stop(struct uv_prepare_s *);
    
    CFFI C function from gevent.libuv._corecffi.lib
    """
    pass

def uv_ref(void, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void uv_ref(void *);
    
    CFFI C function from gevent.libuv._corecffi.lib
    """
    pass

def uv_run(struct_uv_loop_s, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int uv_run(struct uv_loop_s *, uv_run_mode);
    
    CFFI C function from gevent.libuv._corecffi.lib
    """
    pass

def uv_signal_init(struct_uv_loop_s, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int uv_signal_init(struct uv_loop_s *, struct uv_signal_s *);
    
    CFFI C function from gevent.libuv._corecffi.lib
    """
    pass

def uv_signal_start(struct_uv_signal_s, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int uv_signal_start(struct uv_signal_s *, void(*)(struct uv_signal_s *, int), int);
    
    CFFI C function from gevent.libuv._corecffi.lib
    """
    pass

def uv_signal_stop(struct_uv_signal_s, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int uv_signal_stop(struct uv_signal_s *);
    
    CFFI C function from gevent.libuv._corecffi.lib
    """
    pass

def uv_stop(struct_uv_loop_s, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void uv_stop(struct uv_loop_s *);
    
    CFFI C function from gevent.libuv._corecffi.lib
    """
    pass

def uv_strerror(p_int): # real signature unknown; restored from __doc__
    """
    char *uv_strerror(int);
    
    CFFI C function from gevent.libuv._corecffi.lib
    """
    pass

def uv_timer_again(struct_uv_timer_s, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int uv_timer_again(struct uv_timer_s *);
    
    CFFI C function from gevent.libuv._corecffi.lib
    """
    pass

def uv_timer_get_repeat(struct_uv_timer_s, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    uint64_t uv_timer_get_repeat(struct uv_timer_s *);
    
    CFFI C function from gevent.libuv._corecffi.lib
    """
    pass

def uv_timer_init(struct_uv_loop_s, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int uv_timer_init(struct uv_loop_s *, struct uv_timer_s *);
    
    CFFI C function from gevent.libuv._corecffi.lib
    """
    pass

def uv_timer_set_repeat(struct_uv_timer_s, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void uv_timer_set_repeat(struct uv_timer_s *, uint64_t);
    
    CFFI C function from gevent.libuv._corecffi.lib
    """
    pass

def uv_timer_start(struct_uv_timer_s, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int uv_timer_start(struct uv_timer_s *, void(*)(struct uv_timer_s *), uint64_t, uint64_t);
    
    CFFI C function from gevent.libuv._corecffi.lib
    """
    pass

def uv_timer_stop(struct_uv_timer_s, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int uv_timer_stop(struct uv_timer_s *);
    
    CFFI C function from gevent.libuv._corecffi.lib
    """
    pass

def uv_unref(void, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void uv_unref(void *);
    
    CFFI C function from gevent.libuv._corecffi.lib
    """
    pass

def uv_update_time(struct_uv_loop_s, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void uv_update_time(struct uv_loop_s *);
    
    CFFI C function from gevent.libuv._corecffi.lib
    """
    pass

def uv_version_string(): # real signature unknown; restored from __doc__
    """
    char *uv_version_string();
    
    CFFI C function from gevent.libuv._corecffi.lib
    """
    pass

def uv_walk(struct_uv_loop_s, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void uv_walk(struct uv_loop_s *, void(*)(struct uv_handle_s *, void *), void *);
    
    CFFI C function from gevent.libuv._corecffi.lib
    """
    pass

def _gevent_async_callback0(struct_uv_async_s, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void _gevent_async_callback0(struct uv_async_s *);
    
    CFFI C function from gevent.libuv._corecffi.lib
    """
    pass

def _gevent_check_callback0(struct_uv_check_s, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void _gevent_check_callback0(struct uv_check_s *);
    
    CFFI C function from gevent.libuv._corecffi.lib
    """
    pass

def _gevent_fs_event_callback3(struct_uv_fs_event_s, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void _gevent_fs_event_callback3(struct uv_fs_event_s *, char *, int, int);
    
    CFFI C function from gevent.libuv._corecffi.lib
    """
    pass

def _gevent_fs_poll_callback3(struct_uv_fs_poll_s, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void _gevent_fs_poll_callback3(struct uv_fs_poll_s *, int, uv_stat_t *, uv_stat_t *);
    
    CFFI C function from gevent.libuv._corecffi.lib
    """
    pass

def _gevent_idle_callback0(struct_uv_idle_s, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void _gevent_idle_callback0(struct uv_idle_s *);
    
    CFFI C function from gevent.libuv._corecffi.lib
    """
    pass

def _gevent_poll_callback2(struct_uv_poll_s, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void _gevent_poll_callback2(struct uv_poll_s *, int, int);
    
    CFFI C function from gevent.libuv._corecffi.lib
    """
    pass

def _gevent_prepare_callback0(struct_uv_prepare_s, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void _gevent_prepare_callback0(struct uv_prepare_s *);
    
    CFFI C function from gevent.libuv._corecffi.lib
    """
    pass

def _gevent_signal_callback1(struct_uv_signal_s, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void _gevent_signal_callback1(struct uv_signal_s *, int);
    
    CFFI C function from gevent.libuv._corecffi.lib
    """
    pass

def _gevent_timer_callback0(struct_uv_timer_s, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void _gevent_timer_callback0(struct uv_timer_s *);
    
    CFFI C function from gevent.libuv._corecffi.lib
    """
    pass

# no classes
