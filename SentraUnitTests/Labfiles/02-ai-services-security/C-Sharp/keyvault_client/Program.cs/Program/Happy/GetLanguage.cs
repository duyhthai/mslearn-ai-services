using System;
using Microsoft.VisualStudio.TestTools.UnitTesting;
using Moq;

namespace UnitTests
{
    [TestClass]
    public class ProgramTests
    {
        private const string aiSvcKey = "your_ai_svc_key";
        private const string aiSvcEndpoint = "your_ai_svc_endpoint";

        [TestMethod]
        public void GetLanguage_WithValidText_ReturnsDetectedLanguage()
        {
            // Arrange
            string text = "Hello, how are you?";
            var mockClient = new Mock<TextAnalyticsClient>();
            mockClient.Setup(client => client.DetectLanguage(It.IsAny<string>()))
                      .Returns(new DetectedLanguage("English", "en"));

            Program.aiSvcKey = aiSvcKey;
            Program.aiSvcEndpoint = aiSvcEndpoint;

            // Act
            string result = Program.GetLanguage(text);

            // Assert
            Assert.AreEqual("English", result);
        }

        [TestMethod]
        public void GetLanguage_WithEmptyText_ReturnsUnknownLanguage()
        {
            // Arrange
            string text = "";
            var mockClient = new Mock<TextAnalyticsClient>();
            mockClient.Setup(client => client.DetectLanguage(It.IsAny<string>()))
                      .Returns(new DetectedLanguage("", ""));

            Program.aiSvcKey = aiSvcKey;
            Program.aiSvcEndpoint = aiSvcEndpoint;

            // Act
            string result = Program.GetLanguage(text);

            // Assert
            Assert.AreEqual("", result);
        }

        [TestMethod]
        public void GetLanguage_WithNullText_ReturnsUnknownLanguage()
        {
            // Arrange
            string text = null;
            var mockClient = new Mock<TextAnalyticsClient>();
            mockClient.Setup(client => client.DetectLanguage(It.IsAny<string>()))
                      .Returns(new DetectedLanguage("", ""));

            Program.aiSvcKey = aiSvcKey;
            Program.aiSvcEndpoint = aiSvcEndpoint;

            // Act
            string result = Program.GetLanguage(text);

            // Assert
            Assert.AreEqual("", result);
        }
    }
}