import data from "../data";
import exampleData from "../exampleData";

const start = process.hrtime();

function boardingPassCheck(input: string[]) {
    let seatIds = [];
    for(let i=0; i < input.length; i++) {
        let rows = Array.from({length: 128}, (x, i) => i);
        let cols = Array.from({length: 8}, (x, i) => i);

        input[i].split("").filter(x => {
            let rowsMid = rows.length / 2;
            let colsMid = cols.length / 2;

            switch(x) {
                case "F":
                    rows = rows.slice(0, rowsMid);
                    break;
                case "B":
                    rows = rows.slice(rowsMid);
                    break;
                case "L":
                    cols = cols.slice(0, colsMid);
                    break;
                case "R":
                    cols = cols.slice(colsMid);
                    break;
            }
        });
        
        seatIds.push((rows[0] * 8) + cols[0]);
    }
    return Math.max(...seatIds);
}
console.log("Puzzle answer: " + boardingPassCheck(data));

const end = process.hrtime(start);
console.info('Execution time: %ds %dms', end[0], end[1] / 1000000);