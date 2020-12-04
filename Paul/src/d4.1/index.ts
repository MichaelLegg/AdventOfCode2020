import { timeExecutionAsync } from "../utility";
import { createReadStream } from "fs";
import { createInterface } from "readline";

async function solution() {
  const data = createReadStream("./src/d4.1/data.txt");

  const rl = createInterface({
    input: data,
    crlfDelay: Infinity,
  });

  const reqs = ["eyr", "hcl", "ecl", "iyr", "byr", "pid", "hgt"];
  let currentPassport = [];
  let validPassports = [];

  for await (const line of rl) {
    if (line === "") {
      const valid = reqs.every((i) => {
        return currentPassport.includes(i);
      });
      if (valid) {
        validPassports.push([...currentPassport.sort(), valid]);
      }
      currentPassport = [];
    } else {
      line.split(" ").forEach((s) => currentPassport.push(s.split(":")[0]));
    }
  }

  const valid = reqs.every((i) => {
    return currentPassport.includes(i);
  });
  if (valid) {
    validPassports.push([...currentPassport.sort(), valid]);
  }

  return validPassports.length;
}

timeExecutionAsync(() => solution()).then((r) => console.log(r));
