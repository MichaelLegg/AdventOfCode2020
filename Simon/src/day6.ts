import { AdventDay, getInputLines } from "./common";

export default {
	part1(input: string[]): number {
		return input.reduce(
			(p, n) =>
				p +
				n
					.replace(/\s/g, "")
					.split("")
					.reduce((a, b) => a.add(b), new Set<string>()).size,
			0
		);
	},
	part2(input: string[]): number {
		throw new Error("not implemented");
	},
	async getInput(file: string) {
		return await getInputLines(file, "\r\n\r\n");
	},
} as AdventDay<string[]>;
