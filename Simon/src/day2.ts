import { AdventDay, getInputLines } from "./common";

export default {
	part1(inputs: string[]): number {
		const valid = inputs.filter((pwd) => {
			const m = /(\d+)-(\d+) (\w): (.*)/.exec(pwd);
			if (!m) {
				throw new Error("Invalid entry: " + pwd);
			}
			const min = +m[1];
			const max = +m[2];
			const char = m[3];
			const text = m[4];
			const split = (text.match(new RegExp(char, "g")) || []).length;
			return split >= min && split <= max;
		});
		return valid.length;
	},
	part2(inputs: string[]): number {
		const valid = inputs.filter((pwd) => {
			const m = /(\d+)-(\d+) (\w): (.*)/.exec(pwd);
			if (!m) {
				throw new Error("Invalid entry: " + pwd);
			}
			const posA = +m[1];
			const posB = +m[2];
			const char = m[3];
			const text = m[4];
			return +(text[posA - 1] === char) ^ +(text[posB - 1] === char);
		});
		return valid.length;
	},
	async getInput(file: string) {
		return await getInputLines(file);
	},
} as AdventDay<string[]>;
