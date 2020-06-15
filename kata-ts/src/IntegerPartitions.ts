function prod(n: number) {
  let set: Set<number> = new Set();
  function splitArry(n: number): number[][] {
    if (n == 1) {
      return [[1]];
    } else {
      let arr = splitArry(n - 1)
      let merge = []
      let lastItem = [...arr[arr.length - 1], 1]

      arr.forEach((sub: number[], i) => {
        let tmp = [...sub]
        if (i > 0) {
          for (let j = 0; j < sub.length; j++) {
            let tmp2 = [...tmp]
            tmp2[j] += 1
            merge.push(tmp2)
          }
        } else {
          tmp[i] += 1
          merge.push(tmp)
        }
      })
      merge.push(lastItem)
      console.log(merge);
      return merge;
    }
  }
  let generated = splitArry(n);

  for (let i = 0; i < generated.length; i++) {
    let numb = generated[i].reduce((a, b) => a * b)
    set.add(numb);
  }


  let res: number[] = Array.from(set);
  res.sort((a, b) => a - b);
  let average = ((res.reduce((a, b) => a + b)) / res.length).toFixed(2);
  let median = ((res[(res.length - 1) >> 1] + res[res.length >> 1]) / 2).toFixed(2);
  let range = res[res.length - 1] - 1;
  return "Range: " + range + " Average: " + average + " Median: " + median;
}


function test() {
  console.log(prod(9));
}
export { test };
