
const fs = require('fs')

fs.readFile('DataInput.txt', (err, data) => {
    if(err) throw err;

    console.log(data.toString());

})
