import { AdventDay, getInputLines } from "./common";

export default {
	part1(input: number[]): number {
		const pLen = input.shift()!;
		for (let i = pLen; i < input.length; i++) {
			const target = input[i];
			let found = false;
			for (let j = i - pLen; j < i; j++) {
				for (let k = j + 1; k < i; k++) {
					if (input[j] + input[k] === target) {
						found = true;
						break;
					}
				}
				if (found) break;
			}
			if (!found) {
				return target;
			}
		}

		throw "result not found";
	},
	part2(input: number[]): number {
		const target = this.part1(input);
		for (let i = 0; i < input.length; i++) {
			let s = 0;
			let j = i;
			while (s < target) {
				s += input[j++];
			}
			if (s === target) {
				const v = input.slice(i, j).sort((a, b) => a - b);
				return v[0] + v[v.length - 1];
			}
		}
		throw "result not found";
	},
	async getInput(file: string) {
		return (await getInputLines(file, "\r\n")).map(Number);
	},
} as AdventDay<number[]>;
