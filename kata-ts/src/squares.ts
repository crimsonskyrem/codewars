function decompose(int: number): number[] {
  let res: number[] = [];
  let lefts: number[] = [];
  let left = int ** 2;
  let factor = int - 1;
  res.push(factor);
  lefts.push(left);
  while (left > 0) {
    left -= factor ** 2;
    factor = Math.floor(Math.sqrt(left));
    if (res.indexOf(factor) > 0 || factor >= res[res.length - 1]) {
      res.pop();
      lefts.pop();
      factor = res.pop() - 1;
      left = lefts.pop();
    }
    lefts.push(left);
    if (factor > 0) {
      res.push(factor);
    }
  }
  if (left == 0) {
    return res.sort((a, b) => a - b);
  }

  return [];
}

function test() {
  // 5 [4, 3] 25 9
  // 7 [6, 3, 2] 13 4
  // 10 [8, 6] 36
  // 11 [10, 4, 2, 1] 21 5 1
  // 50 [49, 8, 5, 3, 1]  99 35 10
  // 50 [49, 9, 4, 1, 1]  99 18 2 1
  // 52 [50, 13, 5, 3, 1] 204 35 10
  console.log(decompose(1));
}
export { test };
