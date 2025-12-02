const std: type = @import("std");

fn isRepeatingSequence(s: []const u8) bool {
    const n = s.len;
    if (n < 2) {
        return false;
    }

    var pattern_len: usize = 1;
    while (pattern_len <= n / 2) : (pattern_len += 1) {
        if (n % pattern_len == 0) {
            const pattern = s[0..pattern_len];
            const num_repeats = n / pattern_len;

            var i: usize = 1;
            while (i < num_repeats) : (i += 1) {
                const next_segment = s[i * pattern_len .. (i + 1) * pattern_len];
                if (!std.mem.eql(u8, pattern, next_segment)) {
                    break;
                }
                if (i == num_repeats - 1) {
                    return true;
                }
            }
        }
    }

    return false;
}

pub fn main() !void {
    var t: std.time.Timer = try std.time.Timer.start();

    const file: std.fs.File = try std.fs.cwd().openFile("./day_2/input.txt", .{ .mode = .read_only });
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
            var buf: [64]u8 = undefined;
            const number_str = try std.fmt.bufPrint(&buf, "{d}", .{number});

            if (isRepeatingSequence(number_str)) {
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
