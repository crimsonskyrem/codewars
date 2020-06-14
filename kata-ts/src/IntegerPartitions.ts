function prod(int: number) {
  let arr: number[] = [];
  for (let i = 1; i <= n; i++) {
    arr.push(1);
  }
  let set: Set<number> = new Set();
  let generated = splitArry(arr);
  set.add(1);

  for (let i = 0; i < generated.length; i++) {
    let numb = generated[i].reduce((a, b) => a * b)
    set.add(numb);
  }

  function splitArry(arr: number[]): number[][] {
    let length = arr.length;
    let exists: number[] = [];
    if (length < 3) {
      return [arr];
    }
    let res: number[][] = [];
    for (let i = 1; i < length; i++) {
      let tmp: number[] = [];
      let copy = [...arr];
      let rest = copy.splice(0, i);
      if (rest.length > 1) {
        let copyNum = copy.reduce((a, b) => a + b);
        tmp.push(copyNum);
        let restArr = splitArry([...rest]);
        if (restArr.length > 0) {
          restArr.forEach(sub => {
            let tmparr = [...sub, copyNum];
            if (chk(tmparr, exists)) {
              res.push(tmparr);
            }
            let another = [...tmp];
            another.push(sub.reduce((a, b) => a + b))
            if (chk(another, exists)) {
              res.push(another);
            }
          })
        }
      }

      if (chk(tmp, exists)) {
        res.push(tmp)
      }
    }
    return res;
  }
  function chk(arr: number[], include: number[]): Boolean {
    if (arr.length < 1) {
      return false;
    }
    let production = arr.reduce((a, b) => a * b)
    if (include.indexOf(production) > 0) {
      return false;
    } else {
      include.push(production);
      return true;
    }
  }

  let res: number[] = Array.from(set);
  res.sort((a, b) => a - b);
  let average = ((res.reduce((a, b) => a + b)) / res.length).toFixed(2);
  let median = ((res[(res.length - 1) >> 1] + res[res.length >> 1]) / 2).toFixed(2);
  let range = res[res.length - 1] - 1;
  return "Range: " + range + " Average: " + average + " Median: " + median;
}


function test() {
  console.log(prod(8));
}
export { test };
