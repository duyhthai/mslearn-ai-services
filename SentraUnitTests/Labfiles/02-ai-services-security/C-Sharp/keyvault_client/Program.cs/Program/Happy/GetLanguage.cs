using Microsoft.VisualStudio.TestTools.UnitTesting;
using System;

[TestClass]
public class ProgramTests
{
    [TestMethod]
    public void GetLanguage_WithValidText_ReturnsCorrectLanguage()
    {
        // Arrange
        string aiSvcKey = "your_key_here";
        string aiSvcEndpoint = "your_endpoint_here";
        string inputText = "Hello, world!";
        string expectedLanguage = "English";

        // Act
        string result = Program.GetLanguage(inputText);

        // Assert
        Assert.AreEqual(expectedLanguage, result);
    }

    [TestMethod]
    public void GetLanguage_WithAnotherValidText_ReturnsCorrectLanguage()
    {
        // Arrange
        string aiSvcKey = "your_key_here";
        string aiSvcEndpoint = "your_endpoint_here";
        string inputText = "Bonjour le monde!";
        string expectedLanguage = "French";

        // Act
        string result = Program.GetLanguage(inputText);

        // Assert
        Assert.AreEqual(expectedLanguage, result);
    }

    [TestMethod]
    public void GetLanguage_WithEmptyText_ReturnsUnknownLanguage()
    {
        // Arrange
        string aiSvcKey = "your_key_here";
        string aiSvcEndpoint = "your_endpoint_here";
        string inputText = "";
        string expectedLanguage = "Unknown";

        // Act
        string result = Program.GetLanguage(inputText);

        // Assert
        Assert.AreEqual(expectedLanguage, result);
    }
}