export function timeExecution(solution: () => any) {
    const start = process.hrtime();
    const data = solution();
    const end = process.hrtime(start);
    console.info("Execution time: %ds %dms", end[0], end[1] / 1000000);

    return data;
}

export async function timeExecutionAsync(solution: () => Promise<any>) {
    const start = process.hrtime();
    const data = await solution();
    const end = process.hrtime(start);
    console.info("Execution time: %ds %dms", end[0], end[1] / 1000000);

    return data;
}