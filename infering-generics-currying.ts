type Params<F extends (...args: any[]) => any> = F extends (
	...args: infer A
) => any
	? A
	: never;

const fn00 = (name: string, age: number, single: boolean) => true;

type parameters = Params<typeof fn00>; // [string, number, boolean]

type Head<T extends any[]> = T extends [any, ...any[]] ? T[0] : never;

type test1 = Head<[1, "hi", 5]>; // 1

type test2 = Head<Params<typeof fn00>>; //string

type Tail<T extends any[]> = ((...t: T) => any) extends (
	_: any,
	...tail: infer TT
) => any
	? TT
	: [];

type test3 = Tail<[1, "hi", 5]>; // ['hi', 5]

type test4 = Head<Tail<Params<typeof fn00>>>; // number

type test5 = Tail<[1, 2, string, number]>; // [2, string, number]

type HasTail<T extends any[]> = T extends [] | [any] ? false : true;

type test6 = HasTail<[1, 2, string, number]>; //true

type test7 = HasTail<[]>; // false

type ObjectInfer<O> = O extends { a: infer A } ? A : never;

const object = { a: "Hello" };

type test8 = ObjectInfer<typeof object>; //string

type test9 = ObjectInfer<string>; // never

type FunctionInfer<F> = F extends (...args: infer A) => infer B
	? [A, B]
	: never;

type test10 = FunctionInfer<typeof fn00>; // [[string, number, boolean], boolean]

type ClassInfer<I> = I extends Promise<infer G> ? G : never;

const promise = new Promise<string>(() => {});

type test11 = ClassInfer<typeof promise>; // string

type ArrayInfer<T> = T extends (infer U)[] ? U : never;

const array = [1, "data", 2, "bye"];

type test12 = ArrayInfer<typeof array>; // string | number

type TupleInfer<T> = T extends [infer A, ...(infer B)[]] ? [A, B] : never;

type test13 = TupleInfer<[string, number, boolean]>; // [string, number | boolean]

type CurryV0<T extends any[], R> = (
	arg0: Head<T>
) => HasTail<T> extends true ? CurryV0<Tail<T>, R> : R;

declare function curryV0<P extends any[], R>(f: (...args: P) => R): CurryV0<P, R>

const curried00 = curryV0(fn00);
const test14 = curried00('Taghi')(25)(true) //boolean