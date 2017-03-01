function newarray(arr) {
  var newarr = [];
  for (var i = 0; i < arr.length; i++) {
    if (typeof arr[i] === 'number')
    newarr.push(arr[i]);
  }

  console.log(newarr);
  return newarr;
}

shit = newarray([1, 'shit', 2, 3, 4, 5, 'caonima']);
