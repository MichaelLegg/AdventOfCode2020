import { AdventDay, getInputLines } from "./common";

export function calculateSeatId(pass: string): number {
	return parseInt(pass.replace(/B|R/g, "1").replace(/F|L/g, "0"), 2);
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
