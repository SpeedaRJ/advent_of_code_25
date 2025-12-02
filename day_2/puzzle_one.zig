const std: type = @import("std");

pub fn main() !void {
    var t: std.time.Timer = try std.time.Timer.start();

    const file: std.fs.File = try std.fs.cwd().openFile("day_2/input.txt", .{ .mode = .read_only });
    defer file.close();

    var buffer: [65536]u8 = undefined;
    const bytes_read: usize = try file.readAll(&buffer);
    const content: []const u8 = std.mem.trim(u8, buffer[0..bytes_read], "\x00");

    var sum: i64 = 0;

    var lines = std.mem.splitScalar(u8, content, ',');

    while (lines.next()) |line| {
        var limits = std.mem.splitScalar(u8, line, '-');
        const start = try std.fmt.parseInt(i64, limits.next().?, 10);
        const end = try std.fmt.parseInt(i64, limits.next().?, 10);

        var number: i64 = start;
        while (number < end + 1) {
            var buf: [20]u8 = undefined;
            const number_str = try std.fmt.bufPrint(&buf, "{d}", .{number});
            if (@mod(number_str.len, 2) == 0 and std.mem.eql(u8, number_str[0 .. number_str.len / 2], number_str[number_str.len / 2 ..])) {
                sum += number;
            }
            number += 1;
        }
    }

    std.debug.print("Total sum: '{d}'\n", .{sum});

    const elapsed2: f64 = @floatFromInt(t.read());
    std.debug.print("Time elapsed is: {d:.3}ms\n", .{
        elapsed2 / std.time.ns_per_ms,
    });
}
