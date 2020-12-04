// BROKEN

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
  const rules = {
    byr: (s: string) => {
      const v = Number(s) >= 1920 && Number(s) <= 2002;
      if (!v) console.log("byr", s, v);
      return v;
    },
    iyr: (s: string) => {
      const v = Number(s) >= 2010 && Number(s) <= 2020;
      if (!v) console.log("iyr", s, v);
      return validPassports;
    },
    eyr: (s: string) => {
      const v = Number(s) >= 2020 && Number(s) <= 2030;
      if (!v) console.log("eyr", s, v);
      return v;
    },
    hgt: (s: string) => {
      let v = false;
      if (s.includes("cm")) {
        const val = Number(s.substr(0, s.length - 2));
        v = val >= 150 && val <= 193;
      }
      if (s.includes("in")) {
        const val = Number(s.substr(0, s.length - 2));
        v = val >= 59 && val <= 76;
      }

      if (!v) console.log("hgt", s, v);

      return v;
    },
    hcl: (s: string) => {
      if (!s.startsWith("#")) {
        console.log("hcl", s, "start", false);
        return false;
      } else {
        const val = s.substr(1);
        const v = val.length === 6 && /[0-9a-f]{6}/.test(val);
        if (!v) console.log("hcl", s, v);
        return v;
      }
    },
    ecl: (s: string) => {
      const v = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"].includes(s);
      if (!v) console.log("ecl", s, v);
      return v;
    },
    pid: (s: string) => {
      const v = s.length === 9 && /\d{9}/.test(s);
      if (!v) console.log("pid", s, v);
      return v;
    },
  };
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
      line.split(" ").forEach((s) => {
        const items = s.split(":");
        if (rules[items[0]] && rules[items[0]](items[1])) {
          currentPassport.push(items[0]);
        }
      });
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
