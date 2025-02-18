using NUnit.Framework;
using Moq;
using System;

[TestFixture]
public class ProgramTests
{
    private const string aiSvcKey = "your-ai-svc-key";
    private const string aiSvcEndpoint = "https://your-ai-svc-endpoint.cognitiveservices.azure.com";

    [Test]
    public void GetLanguage_ThrowsException_WhenTextIsNull()
    {
        // Arrange
        Program program = new Program();
        string text = null;

        // Act & Assert
        Assert.ThrowsAsync<ArgumentNullException>(() => program.GetLanguage(text));
    }

    [Test]
    public void GetLanguage_ThrowsException_WhenAzureKeyCredentialIsNull()
    {
        // Arrange
        Program program = new Program();
        string text = "test text";
        Mock<TextAnalyticsClient> mockClient = new Mock<TextAnalyticsClient>(new Uri(aiSvcEndpoint), null);

        // Act & Assert
        Assert.ThrowsAsync<InvalidOperationException>(() => program.GetLanguage(text));
    }

    [Test]
    public void GetLanguage_ThrowsException_WhenDetectLanguageFails()
    {
        // Arrange
        Program program = new Program();
        string text = "test text";
        Mock<TextAnalyticsClient> mockClient = new Mock<TextAnalyticsClient>(new Uri(aiSvcEndpoint), new AzureKeyCredential(aiSvcKey));
        mockClient.Setup(client => client.DetectLanguage(It.IsAny<string>())).Throws(new RequestFailedException("Mocked error"));

        // Act & Assert
        Assert.ThrowsAsync<RequestFailedException>(() => program.GetLanguage(text));
    }
}