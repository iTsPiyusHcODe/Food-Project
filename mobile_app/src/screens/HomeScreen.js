import React, { useState, useEffect } from 'react';
import { View, StyleSheet, FlatList, ScrollView } from 'react-native';
import { Text, Card, Title, Paragraph, Button, Searchbar, Chip, ActivityIndicator } from 'react-native-paper';
import { recipeAPI } from '../api/api';

const HomeScreen = ({ navigation }) => {
  const [featuredRecipes, setFeaturedRecipes] = useState([]);
  const [categories, setCategories] = useState([]);
  const [searchQuery, setSearchQuery] = useState('');
  const [loading, setLoading] = useState(true);

  // Fetch data on component mount
  useEffect(() => {
    const fetchData = async () => {
      try {
        // In a real app, these would be actual API calls
        // For now, we'll use mock data
        
        // Simulate API call delay
        await new Promise(resolve => setTimeout(resolve, 1000));
        
        // Mock featured recipes
        setFeaturedRecipes([
          {
            id: 1,
            title: 'Spaghetti Carbonara',
            description: 'Classic Italian pasta dish with eggs, cheese, pancetta, and pepper.',
            image: 'https://example.com/carbonara.jpg',
            cooking_time: 30,
            category: { name: 'Italian' },
            price: 12.99,
            available_for_order: true,
          },
          {
            id: 2,
            title: 'Chicken Tikka Masala',
            description: 'Grilled chicken chunks in spiced curry sauce.',
            image: 'https://example.com/tikka.jpg',
            cooking_time: 45,
            category: { name: 'Indian' },
            price: 14.99,
            available_for_order: true,
          },
          {
            id: 3,
            title: 'Avocado Toast',
            description: 'Simple and delicious breakfast with mashed avocado on toasted bread.',
            image: 'https://example.com/avocado.jpg',
            cooking_time: 10,
            category: { name: 'Breakfast' },
            price: 8.99,
            available_for_order: true,
          },
        ]);
        
        // Mock categories
        setCategories([
          { id: 1, name: 'Italian' },
          { id: 2, name: 'Indian' },
          { id: 3, name: 'Chinese' },
          { id: 4, name: 'Mexican' },
          { id: 5, name: 'Breakfast' },
          { id: 6, name: 'Dessert' },
        ]);
        
        setLoading(false);
      } catch (error) {
        console.error('Error fetching data:', error);
        setLoading(false);
      }
    };
    
    fetchData();
  }, []);

  const onChangeSearch = query => setSearchQuery(query);
  
  const handleRecipePress = (recipe) => {
    navigation.navigate('RecipeDetail', { recipeId: recipe.id });
  };
  
  const handleCategoryPress = (category) => {
    navigation.navigate('Recipes', { categoryId: category.id });
  };
  
  const handleSearch = () => {
    navigation.navigate('Recipes', { searchQuery });
  };

  if (loading) {
    return (
      <View style={styles.loadingContainer}>
        <ActivityIndicator size="large" color="#ff6b6b" />
        <Text style={styles.loadingText}>Loading...</Text>
      </View>
    );
  }

  return (
    <ScrollView style={styles.container}>
      {/* Header */}
      <View style={styles.header}>
        <Text style={styles.headerTitle}>Foodie App</Text>
        <Text style={styles.headerSubtitle}>Discover & Order Delicious Food</Text>
      </View>
      
      {/* Search Bar */}
      <Searchbar
        placeholder="Search recipes..."
        onChangeText={onChangeSearch}
        value={searchQuery}
        style={styles.searchBar}
        onSubmitEditing={handleSearch}
      />
      
      {/* Categories */}
      <View style={styles.sectionContainer}>
        <Text style={styles.sectionTitle}>Categories</Text>
        <ScrollView horizontal showsHorizontalScrollIndicator={false} style={styles.categoriesContainer}>
          {categories.map(category => (
            <Chip 
              key={category.id} 
              style={styles.categoryChip}
              onPress={() => handleCategoryPress(category)}
            >
              {category.name}
            </Chip>
          ))}
        </ScrollView>
      </View>
      
      {/* Featured Recipes */}
      <View style={styles.sectionContainer}>
        <Text style={styles.sectionTitle}>Featured Recipes</Text>
        <FlatList
          data={featuredRecipes}
          keyExtractor={item => item.id.toString()}
          horizontal
          showsHorizontalScrollIndicator={false}
          renderItem={({ item }) => (
            <Card style={styles.recipeCard} onPress={() => handleRecipePress(item)}>
              <Card.Cover source={{ uri: item.image }} style={styles.recipeImage} />
              <Card.Content>
                <Title numberOfLines={1}>{item.title}</Title>
                <View style={styles.recipeInfo}>
                  <Text style={styles.categoryTag}>{item.category.name}</Text>
                  <Text style={styles.cookingTime}>{item.cooking_time} mins</Text>
                </View>
                <Paragraph numberOfLines={2}>{item.description}</Paragraph>
              </Card.Content>
              <Card.Actions>
                <Button onPress={() => handleRecipePress(item)}>View</Button>
                {item.available_for_order && (
                  <Button 
                    mode="contained"
                    onPress={() => navigation.navigate('Cart', { addItem: item })}
                  >
                    ${item.price}
                  </Button>
                )}
              </Card.Actions>
            </Card>
          )}
        />
      </View>
      
      {/* How It Works */}
      <View style={styles.sectionContainer}>
        <Text style={styles.sectionTitle}>How It Works</Text>
        <View style={styles.howItWorksContainer}>
          <View style={styles.howItWorksItem}>
            <Text style={styles.howItWorksIcon}>🔍</Text>
            <Text style={styles.howItWorksTitle}>Discover</Text>
            <Text style={styles.howItWorksText}>Browse our collection of recipes</Text>
          </View>
          <View style={styles.howItWorksItem}>
            <Text style={styles.howItWorksIcon}>🛒</Text>
            <Text style={styles.howItWorksTitle}>Order</Text>
            <Text style={styles.howItWorksText}>Add your favorites to cart</Text>
          </View>
          <View style={styles.howItWorksItem}>
            <Text style={styles.howItWorksIcon}>🍽️</Text>
            <Text style={styles.howItWorksTitle}>Enjoy</Text>
            <Text style={styles.howItWorksText}>Receive and enjoy your meal</Text>
          </View>
        </View>
      </View>
    </ScrollView>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#f8f8f8',
  },
  loadingContainer: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
  },
  loadingText: {
    marginTop: 10,
    fontSize: 16,
  },
  header: {
    padding: 20,
    paddingTop: 10,
  },
  headerTitle: {
    fontSize: 28,
    fontWeight: 'bold',
    color: '#ff6b6b',
  },
  headerSubtitle: {
    fontSize: 16,
    color: '#666',
    marginTop: 5,
  },
  searchBar: {
    marginHorizontal: 20,
    marginBottom: 20,
    elevation: 2,
  },
  sectionContainer: {
    marginBottom: 20,
  },
  sectionTitle: {
    fontSize: 20,
    fontWeight: 'bold',
    marginHorizontal: 20,
    marginBottom: 10,
  },
  categoriesContainer: {
    paddingHorizontal: 15,
  },
  categoryChip: {
    marginHorizontal: 5,
    backgroundColor: '#fff',
  },
  recipeCard: {
    width: 280,
    marginHorizontal: 10,
    marginBottom: 5,
  },
  recipeImage: {
    height: 150,
  },
  recipeInfo: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    marginVertical: 5,
  },
  categoryTag: {
    color: '#ff6b6b',
    fontWeight: 'bold',
  },
  cookingTime: {
    color: '#666',
  },
  howItWorksContainer: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    paddingHorizontal: 20,
  },
  howItWorksItem: {
    flex: 1,
    alignItems: 'center',
    backgroundColor: '#fff',
    padding: 15,
    borderRadius: 10,
    marginHorizontal: 5,
    elevation: 2,
  },
  howItWorksIcon: {
    fontSize: 30,
    marginBottom: 10,
  },
  howItWorksTitle: {
    fontSize: 16,
    fontWeight: 'bold',
    marginBottom: 5,
  },
  howItWorksText: {
    fontSize: 12,
    textAlign: 'center',
    color: '#666',
  },
});

export default HomeScreen; 