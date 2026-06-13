// 5 kyu
// Limit Async Tasks
// Running asynchronous work with a concurrency limit is a common scheduling problem.
// Sometimes you need to execute many tasks, but you cannot allow all of them to run at once.
// In this kata, you must build a function that runs asynchronous tasks while
//  respecting a maximum number of tasks that may run at the same time.
// You are given:
// tasks: an array of functions
// limit: the maximum number of tasks that may run simultaneously
// When there is available capacity and there are still pending tasks,
// another task must be started immediately.
// Each function in tasks is called only when it is scheduled to run.
// A task normally produces its result asynchronously, but it may also fail
// immediately by throwing an error.
// Your job is to execute tasks while respecting the concurrency limit and
// return an asynchronous result that:
// succeeds with an array of results in the same order as the input tasks
// fails with the same error if any task fails
// Even if some tasks finish earlier than others, the final result must
// preserve the original input order.
// If limit is less than 1, the operation must fail with an error whose message is:
// Invalid limit
// Rules
// tasks is an array of functions
// each task is called only when scheduled
// a task normally completes asynchronously
// a task may also fail immediately by throwing an error
// no more than limit tasks may be running at the same time
// if there is available capacity and there are still pending tasks, another task
//  must be started immediately
// results must keep the original task order
// if tasks is empty, succeed with an empty array
// if any task fails, fail with that same error
// if limit < 1, fail with an error whose message is "Invalid limit"
// Example
// Initial values:

// tasks = [
//   task that completes with "A" after 30 ms,
//   task that completes with "B" after 10 ms,
//   task that completes with "C" after 20 ms
// ]
// limit = 2
// Step-by-step
// Start "A" and "B"
// "B" finishes first
// Start "C"
// "A" finishes
// "C" finishes
// Result
// ["A", "B", "C"]
// Another example
// Initial values:
// tasks = [
//   task that completes with 1,
//   task that completes with 2,
//   task that completes with 3
// ]
// limit = 1
// Step-by-step
// Only one task may run at a time
// Run task 1 -> result 1
// Run task 2 -> result 2
// Run task 3 -> result 3
// Result
// [1, 2, 3]
// Failing task example
// Initial values:
// tasks = [
//   task that completes with 1,
//   task that fails with "boom",
//   task that completes with 3
// ]
// limit = 2
// Step-by-step
// Start the first two tasks
// The second task fails
// The whole process fails with that same error
// Result
// fails with "boom"
// Invalid limit example
// Initial values:
// tasks = [
//   task that completes with 1
// ]
// limit = 0
// Result
// fails with an error whose message is "Invalid limit"

// async function limitAsync(
//   tasks: (() => Promise<any>)[],
//   limit: number,
// ): Promise<any[]> {
//   const res: any[] = [];

//   let running = 0;
//   let index = 0;

//   return new Promise((resolve, reject) => {
//     function tryStartMore() {
//       while (running < limit && index < tasks.length) {
//         running++;
//         const i = index++;
//         const task = tasks[i]();

//         res[i] = task.then((val) => {
//           running--;
//           tryStartMore();
//           res[i] = val;
//           if (running === 0 && index >= tasks.length) {
//             resolve(res);
//           }
//         }).catch(reject);
//       }
//     }

//     tryStartMore();

//     if (running === 0 && index >= tasks.length) {
//       resolve(res);
//     }
//   });
// }


function limitAsync(tasks: (() => Promise<any>)[],limit: number,i=0) {
    if (limit < 1) throw new Error("Invalid limit")
    
    const data: any[] = [], 
         //Create our function which saves the data and do the async work, verify that the current 
         // index is less than the tasks array, execute the task with i and then when the task if finished 
         //pass the work to other worker with i++
          exec = async () => { while (i < tasks.length) data[i] = await tasks[i++]() },
          pool = Array.from({ length: Math.min(limit, tasks.length) }, exec),
          tada = () => data
    
    return Promise
            .all  (pool)
            .then (tada)
  }