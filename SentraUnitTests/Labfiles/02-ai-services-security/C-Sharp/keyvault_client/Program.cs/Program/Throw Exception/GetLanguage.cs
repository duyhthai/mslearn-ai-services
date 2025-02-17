using System;
using Microsoft.Extensions.Configuration;
using Azure.AI.TextAnalytics;
using Azure.Identity;
using Azure.Security.KeyVault.Secrets;
using NUnit.Framework;

[TestFixture]
public class ProgramTests
{
    private const string aiSvcKey = "invalid_key";
    private const string aiSvcEndpoint = "invalid_endpoint";

    [Test]
    public void GetLanguage_InvalidAzureKeyCredential_ThrowsException()
    {
        // Arrange
        string text = "Hello world";
        AzureKeyCredential credentials = new AzureKeyCredential(aiSvcKey);
        Uri endpoint = new Uri(aiSvcEndpoint);
        var client = new TextAnalyticsClient(endpoint, credentials);

        // Act & Assert
        Assert.ThrowsAsync<ArgumentException>(() => client.DetectLanguage(text));
    }

    [Test]
    public void GetLanguage_InvalidUri_ThrowsException()
    {
        // Arrange
        string text = "Hello world";
        AzureKeyCredential credentials = new AzureKeyCredential(aiSvcKey);
        Uri endpoint = new Uri("invalid_uri");
        var client = new TextAnalyticsClient(endpoint, credentials);

        // Act & Assert
        Assert.ThrowsAsync<InvalidOperationException>(() => client.DetectLanguage(text));
    }

    [Test]
    public void GetLanguage_NullText_ThrowsArgumentNullException()
    {
        // Arrange
        string text = null;
        AzureKeyCredential credentials = new AzureKeyCredential(aiSvcKey);
        Uri endpoint = new Uri(aiSvcEndpoint);
        var client = new TextAnalyticsClient(endpoint, credentials);

        // Act & Assert
        Assert.ThrowsAsync<ArgumentNullException>(() => client.DetectLanguage(text));
    }
}