import { createInterface } from "readline";
import { createReadStream} from "fs";
import { isConstructorDeclaration } from "typescript";

async function processLineByLine() {
  const rl = createInterface({
    input: createReadStream("src/day_4/data.txt"),
    crlfDelay: Infinity
  });

  let data = [];
  // let passports = [];
  let passportObj = {};
  let validPassports = 0;

  for await (const line of rl) {
    data.push(line);
  }

  data.forEach((line, idx) => {
    if(line !== "") {
      line.split(" ").forEach(x => passportObj[x.split(":")[0]] = x.split(":")[1]);

      if(idx + 1 === data.length) {
        if(Object.keys(passportObj).length === 8 || (Object.keys(passportObj).length === 7 && passportObj["cid"] === undefined)) validPassports++;
        // passports.push(passportObj);
        passportObj = {};
      }
    } else {
      if(Object.keys(passportObj).length === 8 || (Object.keys(passportObj).length === 7 && passportObj["cid"] === undefined)) validPassports++;
      // passports.push(passportObj);
      passportObj = {};
    }
  });

  return console.log("Puzzle answer: " + validPassports);
}

const start = process.hrtime();

processLineByLine();

const end = process.hrtime(start);
console.info('Execution time: %ds %dms', end[0], end[1] / 1000000);