export type ProblemDetails = {
    type?: string;
    title: string;
    status: number;
    detail?: string;
    instance?: string;
    [key: string]: any;
  };
  
  type ProblemDetailsParams = {
    status: number;
    title: string;
    type?: string;
    detail?: string;
    instance?: string;
    extensions?: Record<string, any>;
  };
  
  const ProblemDetails = {
    create: (params: ProblemDetailsParams): ProblemDetails => {
      const { status, title, type, detail, instance, extensions } = params;
      const problem: ProblemDetails = {
        type,
        title,
        status,
      };
  
      if (type) problem.type = type;
      if (detail) problem.detail = detail;
      if (instance) problem.instance = instance;
      if (extensions) Object.assign(problem, extensions);
  
      return problem;
    },
  };
  
  export { ProblemDetails };