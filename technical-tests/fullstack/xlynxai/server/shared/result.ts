export type SuccessResult<T> = {
    data: T;
    ok: true;
  };
  
  export type ErrorResult = {
    error: {
      message: string;
      code: string;
      stack?: string;
    };
    ok: false;
  };
  
  export type Result<T> = SuccessResult<T> | ErrorResult;
  
  function ok<T>(data: T): Result<T> {
    return {
      data,
      ok: true,
    };
  }
  
  function err(
    message: string,
    code: string,
    stack?: string
  ): ErrorResult {
    return {
      error: {
        message,
        code,
        stack,
      },
      ok: false,
    };
  }

  function isError(result: Result<any>): result is ErrorResult {
    return !result.ok;
  }

  function isSuccess<T>(result: Result<T>): result is SuccessResult<T> {
    return result.ok;
  }
  
  function toThrowable<T>(result: Result<T>) {
    if (result.ok) {
      return result.data;
    }
  
    throw result.error;
  }
  
  export const Result = {
    ok,
    err,
    toThrowable,
    isError,
    isSuccess,
  };