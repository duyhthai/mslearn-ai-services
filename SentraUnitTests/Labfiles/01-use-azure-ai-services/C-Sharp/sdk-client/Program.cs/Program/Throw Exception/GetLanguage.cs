using NUnit.Framework;
using System;

[TestFixture]
public class ProgramTests
{
    [Test]
    public void GetLanguage_ThrowsArgumentException_WhenTextIsNull()
    {
        // Arrange
        string text = null;

        // Act & Assert
        Assert.Throws<ArgumentException>(() => Program.GetLanguage(text));
    }

    [Test]
    public void GetLanguage_ThrowsInvalidOperationException_WhenAzureServiceFails()
    {
        // Arrange
        string text = "test";
        var mockClient = new Mock<TextAnalyticsClient>(MockBehavior.Strict);
        mockClient.Setup(client => client.DetectLanguage(It.IsAny<string>())).Throws(new InvalidOperationException("Simulated error"));
        Program.AISvcClient = mockClient.Object;

        // Act & Assert
        Assert.Throws<InvalidOperationException>(() => Program.GetLanguage(text));
    }

    [Test]
    public void GetLanguage_ReturnsDetectedLanguageName()
    {
        // Arrange
        string text = "Hello world";
        var mockClient = new Mock<TextAnalyticsClient>(MockBehavior.Strict);
        mockClient.Setup(client => client.DetectLanguage(It.IsAny<string>())).Returns(new DetectedLanguage("English", "en", 1.0f));
        Program.AISvcClient = mockClient.Object;

        // Act
        string result = Program.GetLanguage(text);

        // Assert
        Assert.AreEqual("English", result);
    }
}