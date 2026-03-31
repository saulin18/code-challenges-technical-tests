using System.Text.Json;

namespace Currency.Converter;

public class CurrencyApiClient(HttpClient httpClient, ILogger<CurrencyApiClient> logger)
{
    public async Task<decimal?> GetExchangeRateAsync(string currencyCode)
    {
        try
        {
            var response = await httpClient.GetAsync("latest");
            
            if (!response.IsSuccessStatusCode)
            {
                logger.LogWarning("API request failed with status {StatusCode}", response.StatusCode);
                return null;
            }

            var apiResponse = await response.Content.ReadFromJsonAsync<CurrencyApiResponse>(
                new JsonSerializerOptions 
                { 
                    PropertyNameCaseInsensitive = true
                });

            if (apiResponse?.Data != null && 
                apiResponse.Data.TryGetValue(currencyCode.ToUpperInvariant(), out var exchangeRate))
            {
                // Extract the exchange rate from the Value property if available
                return exchangeRate;
            }

            return null;
        }
        catch (Exception ex)
        {
            logger.LogError(ex, "Error fetching exchange rate for {Currency}", currencyCode);
            return null;
        }
    }
}
