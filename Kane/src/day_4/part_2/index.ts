import { createInterface } from "readline";
import { createReadStream} from "fs";

async function processLineByLine() {
  const rl = createInterface({
    input: createReadStream("src/day_4/data.txt"),
    crlfDelay: Infinity
  });

  let data = [];
  let passportObj = {};
  let validPassports = 0;

  for await (const line of rl) {
    data.push(line);
  }

  function isFieldValid(obj: object) {
    let valid: boolean | undefined = true;
    let eyeColours = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"];

    if(Object.keys(obj).length < 7 || (Object.keys(obj).length === 7 && obj["cid"] !== undefined)) valid = false;
    else {
      for(const [k, v] of Object.entries(obj)) {
        switch(k) {
          case "byr":
            if(v.length !== 4 || v < 1920 || v > 2002) valid = false;
            break;
          case "iyr":
            if(v.length !== 4 || v < 2010 || v > 2020) valid = false;
            break;
          case "eyr":
            if(v.length !== 4 || v < 2020 || v > 2030) valid = false;
            break;
          case "hgt":
            if(v.includes("cm") || v.includes("in")) {
              const unit = v.slice(-2);
              const heightVal = v.substring(0, v.length - 2);
              if(unit === "cm") {
                if(heightVal < 150 || heightVal > 193) valid = false;
              } else if(unit === "in") {
                if(heightVal < 59 || heightVal > 76) valid = false;
              }
            } else {
              valid = false;
            }
            break;
          case "hcl":
            if(!v.match(/#[0-9a-f]{6}/)) valid = false;
            break;
          case "ecl":
            if(eyeColours.find(x => x === v) === undefined) valid = false;
            break;
          case "pid":
            if(v.length !== 9) valid = false;
            break;
          case "cid":
            break;
        }
      }
    }

    return valid;
  }

  data.forEach((line, idx) => {
    if(line !== "") {
      line.split(" ").forEach(x => passportObj[x.split(":")[0]] = x.split(":")[1]);

      if(idx + 1 === data.length) {
        if(isFieldValid(passportObj)) validPassports++;
        passportObj = {};
      }
    } else {
      if(isFieldValid(passportObj)) validPassports++;
      passportObj = {};
    }
  });

  return console.log("Puzzle answer: " + validPassports);
}

const start = process.hrtime();

processLineByLine();

const end = process.hrtime(start);
console.info('Execution time: %ds %dms', end[0], end[1] / 1000000);