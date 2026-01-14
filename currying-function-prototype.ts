//Extend the Function prototype with a method wrap() that allows you to wrap an existing function. The method should behave like this:
//
//function speak(name){
//   return "Hello " + name;
//}
//
//const wrapper = speak.wrap(function(original, yourName, myName){
//   const greeting = original(yourName);
//   return greeting + ", my name is " + myName;
//});
//
//wrapper("Mary", "Kate");
//-->
//"Hello Mary, my name is Kate"

// extend the Function object to include a wrap instance method
Object.defineProperty(
    Function.prototype,
    'wrap',
    {value:
        function wrap(wrappedFunc: Function, ...args: unknown[]) {
            const originalFunc = this;
            return function(this: Function, ...innerArgs: unknown[]) {
                return wrappedFunc(originalFunc, ...innerArgs)
            }   
        }
    }
);