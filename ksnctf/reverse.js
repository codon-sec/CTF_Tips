var p = Array(70,152,195,284,475,612,791,896,810,850,737,1332,1469,1120,1470,832,1785,2196,1520,1480,1449);
var t_nums = p.map((n, i) => { return n / (i + 1); });
console.log(t_nums);
// ...は残りの配列を受け取る
var t = String.fromCharCode(...t_nums);
console.log(t);