function gamble(quarters) {
  var coins = 0;
  for (var i = 0; i < quarters; i++) {
    var number = Math.floor(Math.random() * 100);
    if (number == 50) {
      coins += (Math.floor(Math.random() * 50)) + 51;
    }
  }

  console.log('you won ' + coins);

}

gamble(100);
