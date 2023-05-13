using System.Text.Json;
using System.Text.Json.Serialization;

public static class Hash
{
    public static ulong ToHash<T>(T input)
    {
        var bytes = GetBytes(input);
        const ulong prime = 10963707205259UL;
        ulong hash = 14695981039346656037UL;

        for (int i = 0; i < bytes.Length; i++)
        {
            hash ^= bytes[i];
            hash *= prime;
        }

        return hash;
    }

    private static byte[] GetBytes<T>(T input)
    {
        if (typeof(T) == typeof(string))
        {
            return Encoding.UTF8.GetBytes(input as string);
        }
        if (typeof(T) == typeof(byte[]))
        {
            return input as byte[];
        }

        return JsonSerializer.SerializeToUtf8Bytes(input, new JsonSerializerOptions
        {
            DefaultIgnoreCondition = JsonIgnoreCondition.WhenWritingNull
        });
    }
}

