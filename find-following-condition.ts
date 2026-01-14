function findInArray(array: number[], iterator: Function) {
    let mapped = array.findIndex((num, index,) => {
      if (iterator(num, index)) return num
    })  
    
    
    if(!mapped) return -1
     return mapped
   };

