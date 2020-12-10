import { AdventDay, getInputLines } from "./common";

export default {
	part1(input: number[]): number {
		input = [0, ...input.sort((a, b) => a - b), input[input.length - 1] + 3];
		const diffs = { 1: 0, 3: 0 };
		for (let i = 1; i < input.length; i++) {
			diffs[(input[i] - input[i - 1]) as 1]++;
		}
		return diffs[1] * diffs[3];
	},
	part2(input: number[]): number {
		input.sort((a, b) => a - b).unshift(0);
		const m = input.map((v, i) => +(i === 0));
		for (let i = 0; i < input.length; i++) {
			for (let j = Math.max(i - 3, 0); j < i; j++) {
				if (input[i] - input[j] <= 3) {
					m[i] += m[j];
				}
			}
		}
		return m.pop()!;
	},
	async getInput(file: string) {
		return (await getInputLines(file, "\r\n")).map(Number);
	},
} as AdventDay<number[]>;
