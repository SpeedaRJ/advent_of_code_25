const std = @import("std");

pub fn main() !void {
    var t = try std.time.Timer.start();

    const file = try std.fs.cwd().openFile("./day_1/input.txt", .{ .mode = .read_only });
    defer file.close();

    var buffer: [65536]u8 = undefined;
    const bytes_read = try file.readAll(&buffer);
    const content = std.mem.trim(u8, buffer[0..bytes_read], "\x00");

    var dial: i32 = 50;
    var counter: i32 = 0;

    var lines = std.mem.splitScalar(u8, content, '\n');

    while (lines.next()) |line| {
        const direction = line[0..1];
        const distance = try std.fmt.parseInt(i32, std.mem.trim(u8, line[1..], "\r"), 10);

        if (std.mem.eql(u8, direction, "L")) {
            var loops: i32 = 0;
            while (loops < distance) {
                dial = @mod((dial - 1 + 100), 100);
                if (dial == 0) {
                    counter += 1;
                }
                loops += 1;
            }
        } else if (std.mem.eql(u8, direction, "R")) {
            var loops: i32 = 0;
            while (loops < distance) {
                dial = @mod((dial + 1), 100);
                if (dial == 0) {
                    counter += 1;
                }
                loops += 1;
            }
        } else {}
    }

    std.debug.print("Dial landed on 0 '{any}' of times\n", .{counter});

    const elapsed2: f64 = @floatFromInt(t.read());
    std.debug.print("Time elapsed is: {d:.3}ms\n", .{
        elapsed2 / std.time.ns_per_ms,
    });
}
