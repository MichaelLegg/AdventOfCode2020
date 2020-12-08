import { AdventDay, getInputLines } from "./common";

interface Instruction {
	op: "nop" | "acc" | "jmp";
	arg: number;
}

function execute(input: Instruction[]): { acc: number; success: boolean } {
	const seen = new Set<number>();
	let acc = 0;
	for (let i = 0; i < input.length; i++) {
		const cmd = input[i];
		if (seen.has(i)) return { acc, success: false };
		seen.add(i);

		switch (cmd.op) {
			case "nop":
				break;
			case "acc":
				acc += cmd.arg;
				break;
			case "jmp":
				i += cmd.arg - 1;
				break;
			default:
				throw "unknown operation: " + cmd.op;
		}
	}
	return { acc, success: true };
}

export default {
	part1(input: Instruction[]): number {
		return execute(input).acc;
	},
	part2(input: Instruction[]): number {
		for (let i = 0; i < input.length; i++) {
			let cmd: Instruction | null = input[i];
			if (cmd.op === "nop") {
				cmd = { ...cmd, op: "jmp" };
			} else if (cmd.op === "jmp") {
				cmd = { ...cmd, op: "nop" };
			} else {
				cmd = null;
			}
			if (cmd) {
				const modified = [...input];
				modified[i] = cmd;
				const res = execute(modified);
				if (res.success) {
					return res.acc;
				}
			}
		}
		throw "answer not found";
	},
	async getInput(file: string) {
		return (await getInputLines(file, "\r\n")).map((l) => {
			const s = l.split(" ");
			return { op: s[0], arg: +s[1] };
		});
	},
} as AdventDay<Instruction[]>;
