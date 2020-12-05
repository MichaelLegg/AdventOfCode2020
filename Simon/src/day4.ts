import { AdventDay, getInputLines } from "./common";

export default {
	part1(input: string[]): number {
		const required = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"];
		return input.filter((details) => {
			const parts = details
				.split(/ |\n/)
				.map((p) => p.split(":"))
				.reduce((p, n) => {
					p[n[0]] = n[1];
					return p;
				}, {} as Record<string, string>);

			return !required.find((r) => !(r in parts));
		}).length;
	},
	part2(input: string[]): number {
		const required = {
			byr: (v: string) => +v >= 1920 && +v <= 2002,
			iyr: (v: string) => +v >= 2010 && +v <= 2020,
			eyr: (v: string) => +v >= 2020 && +v <= 2030,
			hgt: (v: string) => {
				const m = v.match(/^(\d+)(cm|in)$/);
				if (m) {
					if (m[2] === "cm") {
						return +m[1] >= 150 && +m[1] <= 193;
					} else {
						return +m[1] >= 59 && +m[1] <= 76;
					}
				}
				return false;
			},
			hcl: (v: string) => !!v.match(/^#[0-9a-f]{6}$/),
			ecl: (v: string) => !!v.match(/^amb|blu|brn|gry|grn|hzl|oth$/),
			pid: (v: string) => !!v.match(/^\d{9}$/),
		};

		return input.filter((details) => {
			const parts = details
				.split(/ |\r\n/)
				.map((p) => p.split(":"))
				.reduce((p, n) => {
					p[n[0]] = n[1];
					return p;
				}, {} as Record<string, string>);

			return !Object.keys(required).find(
				(r) => !(r in parts && required[r as keyof typeof required](parts[r]))
			);
		}).length;
	},
	async getInput(file: string) {
		return await getInputLines(file, "\r\n\r\n");
	},
} as AdventDay<string[]>;
