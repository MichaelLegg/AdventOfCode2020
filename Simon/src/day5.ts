import { AdventDay, getInputLines } from "./common";

export function calculateSeatId(pass: string): number {
	return pass
		.split("")
		.reduce((p, n, i) => (n.match(/B|R/) ? p + Math.pow(2, 9 - i) : p), 0);
}

export default {
	part1(input: string[]): number {
		return input.map(calculateSeatId).sort((a, b) => b - a)[0];
	},
	part2(input: string[]): number {
		return 0;
	},
	async getInput(file: string) {
		return await getInputLines(file, "\r\n");
	},
} as AdventDay<string[]>;
