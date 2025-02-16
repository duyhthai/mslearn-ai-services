using System;
using Microsoft.VisualStudio.TestTools.UnitTesting;
using Moq;

[TestClass]
public class ProgramTests
{
    [TestMethod]
    public void GetLanguage_NullText_ThrowsArgumentNullException()
    {
        // Arrange
        string text = null;
        string AISvcKey = "your_key_here";
        string AISvcEndpoint = "your_endpoint_here";

        // Mocking TextAnalyticsClient
        var mockClient = new Mock<TextAnalyticsClient>(MockBehavior.Strict);
        mockClient.Setup(m => m.DetectLanguage(It.IsAny<string>())).Returns(new DetectedLanguage("en", "English"));

        // Replace the actual client with the mocked one
        typeof(Program).GetField("client", BindingFlags.NonPublic | BindingFlags.Static).SetValue(null, mockClient.Object);

        // Act & Assert
        try
        {
            Program.GetLanguage(text);
            Assert.Fail("Expected ArgumentNullException");
        }
        catch (ArgumentNullException ex)
        {
            Assert.AreEqual("text", ex.ParamName);
        }
    }

    [TestMethod]
    public void GetLanguage_EmptyText_ReturnsEmptyString()
    {
        // Arrange
        string text = "";
        string AISvcKey = "your_key_here";
        string AISvcEndpoint = "your_endpoint_here";

        // Mocking TextAnalyticsClient
        var mockClient = new Mock<TextAnalyticsClient>(MockBehavior.Strict);
        mockClient.Setup(m => m.DetectLanguage(It.IsAny<string>())).Returns(new DetectedLanguage("en", "English"));

        // Replace the actual client with the mocked one
        typeof(Program).GetField("client", BindingFlags.NonPublic | BindingFlags.Static).SetValue(null, mockClient.Object);

        // Act
        string result = Program.GetLanguage(text);

        // Assert
        Assert.AreEqual("", result);
    }

    [TestMethod]
    public void GetLanguage_InvalidAISvcKey_ThrowsArgumentException()
    {
        // Arrange
        string text = "Hello World";
        string AISvcKey = ""; // Invalid key
        string AISvcEndpoint = "your_endpoint_here";

        // Mocking TextAnalyticsClient
        var mockClient = new Mock<TextAnalyticsClient>(MockBehavior.Strict);
        mockClient.Setup(m => m.DetectLanguage(It.IsAny<string>())).Returns(new DetectedLanguage("en", "English"));

        // Replace the actual client with the mocked one
        typeof(Program).GetField("client", BindingFlags.NonPublic | BindingFlags.Static).SetValue(null, mockClient.Object);

        // Act & Assert
        try
        {
            Program.GetLanguage(text);
            Assert.Fail("Expected ArgumentException");
        }
        catch (ArgumentException ex)
        {
            Assert.AreEqual("AISvcKey", ex.ParamName);
        }
    }
}