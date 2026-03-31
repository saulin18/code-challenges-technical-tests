using Currency.Converter;

var builder = WebApplication.CreateBuilder(args);

builder.Services.AddOpenApi();

var currencyApiConfig = builder.Configuration.GetSection("CurrencyApi");
var baseUrl = currencyApiConfig["BaseUrl"] ??
              throw new InvalidOperationException("CurrencyApi:BaseUrl is required in configuration");
var apiKey = currencyApiConfig["ApiKey"] ??
             throw new InvalidOperationException("CurrencyApi:ApiKey is required in configuration");

builder.Services.AddHttpClient<CurrencyApiClient>(client =>
{
    client.BaseAddress = new Uri(baseUrl);
    client.DefaultRequestHeaders.Add("apikey", apiKey);
});

var app = builder.Build();

if (app.Environment.IsDevelopment())
{
    app.MapOpenApi();
}

app.UseHttpsRedirection();

app.MapGet("/convert/{currencyCode}", CurrencyConversion.Handle).WithName("ConvertCurrency");

app.Run();
