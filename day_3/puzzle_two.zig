const std: type = @import("std");

pub fn main() !void {
    var t: std.time.Timer = try std.time.Timer.start();

    var gpa = std.heap.GeneralPurposeAllocator(.{}){};
    const allocator = gpa.allocator();

    const file: std.fs.File = try std.fs.cwd().openFile("day_3/input.txt", .{ .mode = .read_only });
    defer file.close();

    var buffer: [65536]u8 = undefined;
    const bytes_read: usize = try file.readAll(&buffer);
    const content: []const u8 = std.mem.trim(u8, buffer[0..bytes_read], "\x00");

    var sum: i64 = 0;

    var lines = std.mem.splitScalar(u8, content, '\n');

    while (lines.next()) |line| {
        var lights: [12]usize = .{ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
        const trimmed_line = std.mem.trim(u8, line, "\r");

        for (0..12) |pos| {
            var start: usize = undefined;
            if (pos == 0) {
                start = 0;
            } else {
                start = lights[pos - 1] + 1;
            }
            const end = trimmed_line.len - 11 + pos;
            const sub_s = trimmed_line[start..end];
            var new_index: usize = 0;
            var s_iter = std.mem.window(u8, sub_s, 1, 1);
            var index_counter: usize = 0;
            while (s_iter.next()) |light| {
                const curr_number = try std.fmt.parseInt(i64, light, 10);
                const ref_number = try std.fmt.parseInt(i64, &[_]u8{sub_s[new_index]}, 10);
                if (curr_number > ref_number) {
                    new_index = index_counter;
                }
                index_counter += 1;
            }
            lights[pos] = new_index + start;
        }

        const lights_value = try std.fmt.allocPrint(allocator, "{c}{c}{c}{c}{c}{c}{c}{c}{c}{c}{c}{c}", .{ trimmed_line[lights[0]], trimmed_line[lights[1]], trimmed_line[lights[2]], trimmed_line[lights[3]], trimmed_line[lights[4]], trimmed_line[lights[5]], trimmed_line[lights[6]], trimmed_line[lights[7]], trimmed_line[lights[8]], trimmed_line[lights[9]], trimmed_line[lights[10]], trimmed_line[lights[11]] });
        sum += try std.fmt.parseInt(i64, lights_value, 10);
    }

    std.debug.print("Total sum: '{d}'\n", .{sum});

    const elapsed2: f64 = @floatFromInt(t.read());
    std.debug.print("Time elapsed is: {d:.3}ms\n", .{
        elapsed2 / std.time.ns_per_ms,
    });
}
