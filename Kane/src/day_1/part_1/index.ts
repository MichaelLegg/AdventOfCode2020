import data from "../data";

for(let i = 0; i < data.length; i++) {
    for(let j = 0; j < data.length; j++) {
        if(data[i] + data[j] === 2020) {
            console.log(data[i] * data[j]);
        }
    }
}