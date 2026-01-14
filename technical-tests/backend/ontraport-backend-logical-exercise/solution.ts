//Write a function that accepts a multi-dimensional container of any size and converts it into a one dimensional associative array whose keys are strings representing their value's path in the original container.
//E.G.
//
//{
//    'one':
//    {
//        'two': 3,
//        'four': [ 5,6,7]
//    },
//    'eight':
//    {
//        'nine':
//        {
//            'ten':11
//        }
//    }
//}
//turns into:
//
//{
//    'one/two':3,
//    'one/four/0':5,
//    'one/four/1':6,
//    'one/four/2':7,
//    'eight/nine/ten':11
//}
//Now write a separate function to do the reverse.


function buildPath(key: string, path: string) {

    let newPath = ''

    if (path !== '') {
        const temp = path + "/" + key
        newPath = temp
    }

    if (path === '') {
        const temp = path += key
        newPath = temp
    }

    return newPath

}

//function solution(obj: any, res: Record<string, any> = {}, path = '') {
//
//           if (typeof obj != "object" || obj === null) {
//               res[path] = obj
//               return res
//           }
//      
//           if (Array.isArray(obj)) {
//               for (let index = 0; index < obj.length; index++) {
//                   const element = obj[index];
//                   const newPath = buildPath(index.toString(), path)
//                   solution(element, res, newPath)
//      
//               }
//      
//           }
//      
//           if (typeof obj === "object") {
//               for (const [key, value] of Object.entries(obj)) {
//      
//                   const newPath = buildPath(key, path)
//      
//                   solution(value, res, newPath)
//               }
//           }
//      
//             return res
//      
//
//    
//
//}

const solution = (obj: any, res: Record<string, any> = {}, path = '') => {

    const queue: [Array<[any, string]>] = [[obj, path]]

    while (queue.length > 0) {

        const arr = queue.pop()

        const [obj, path] = arr?.pop() || [null, ""]



        if (typeof obj != "object" || obj === null) {
            res[path] = obj
            continue
        }

        if (Array.isArray(obj)) {
            for (let index = 0; index < obj.length; index++) {
                const element = obj[index];
                const newPath = buildPath(index.toString(), path)
                queue.push([element, newPath])

            }

        }

        if (typeof obj === "object") {
            for (const [key, value] of Object.entries(obj) as [any, string]) {

                const newPath = buildPath(key, path)

                queue.push([value, newPath])
            }
        }
    }

    return res

}


//2

const solution2 = (objOfPaths: Record<string, any>) => {


    const res = {}


    function recurse(remaining: any, res: Record<any, any>) {

        const queue = Array.from(Object.entries(remaining))

        while (queue.length > 0) {

            let current = res

            const arr = queue.pop()
            const path = arr?.shift() as string
            const value = arr?.pop()


            const keysOfOriginal = path.split("/")

            const finalKey = keysOfOriginal[keysOfOriginal.length - 1]

            for (let i = 0; i < keysOfOriginal.length - 1; i++) {


                const index = keysOfOriginal[i]

                if (!isNaN(Number(index))) {
                    current[Number(index)] = []

                } else if (!Array.isArray(current[index])) {
                    current[index] = {}
                    current = current[index]
                }
            }


            if (!isNaN(Number(finalKey))) {
                current[Number(finalKey)] = value
            } else {
                current[finalKey] = value
            }
        }
    }

    recurse(objOfPaths, res)
    return res
}


//https://github.com/Ontraport/Backend-Test