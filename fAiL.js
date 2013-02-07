var N = 5000000;
var INDEXES = [0, 1, 2, 3, 4, 5];
var chars, num_chars, file;

chars  = "abcdefghikjlmnopqrstuvwxyz";
chars += chars.toUpperCase();
chars += "0123456789";
num_chars = chars.length;

function rand_char() {
    return chars[Math.floor(Math.random() * num_chars)];
}

for (var pos = 0; pos < N; pos++) {
    file = INDEXES.map(rand_char).join('');
    if (file.toLowerCase().indexOf("fail") > -1)
        console.log("hit: " + file + " pos: " + pos);
}
