const load = (day: number) => {
  const formatted = day.toString().padStart(2, "0");
  const path = `../inputs/day${formatted}.txt`;

  return Deno.readTextFileSync(path).split("\n");
};

const take = <T>(n: number, _from: T[]) => {
  if (n >= _from.length) {
    return _from;
  } else {
    return _from.slice(0, n);
  }
};

const slidingWindow = <T>(windowSize: number, _from: T[]) => {
  if (windowSize >= _from.length) {
    return [_from];
  } else {
    const result: T[][] = [];
    for (let i = 0; i < _from.length - windowSize + 1; i++) {
      result.push(_from.slice(i, i + windowSize));
    }
    return result;
  }
};

const maxN = (_from: number[], n: number) => {
  return _from
    .slice(0)
    .sort((a, b) => b - a)
    .slice(0, n);
};

const minN = (_from: number[], n: number) => {
  return _from
    .slice(0)
    .sort((a, b) => a - b)
    .slice(0, n);
};

const split = <T>(_from: T[], by: (t: T) => boolean, keep = false) => {
  const result: T[][] = [];
  let tmp: T[] = [];

  _from.forEach((v) => {
    if (by(v)) {
      if (keep) {
        tmp.push(v);
      }
      result.push(tmp);
      tmp = [];
    } else {
      tmp.push(v);
    }
  });
  return result;
};
