export function on<T extends Window | Document | HTMLElement | EventTarget>(
    obj: T | null,
    ...args: Parameters<T["addEventListener"]> | [string, Function, null, ...any]
  ) {
    if (obj?.addEventListener) {
      obj.addEventListener(
        ...(args as Parameters<HTMLElement["addEventListener"]>)
      );
    }
  }
  
  export function off<T extends Window | Document | HTMLElement | EventTarget>(
    obj: T | null,
    ...args:
      | Parameters<T["removeEventListener"]>
      | [string, Function | null, ...any]
  ) {
    if (obj?.removeEventListener) {
      obj.removeEventListener(
        ...(args as Parameters<HTMLElement["removeEventListener"]>)
      );
    }
  }