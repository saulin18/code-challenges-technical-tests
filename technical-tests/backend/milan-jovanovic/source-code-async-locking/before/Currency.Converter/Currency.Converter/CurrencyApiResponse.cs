using System.Text.Json.Serialization;

namespace Currency.Converter;

public class CurrencyApiResponse
{
    [JsonPropertyName("data")]
    public Dictionary<string, decimal> Data { get; init; } = new();
}
