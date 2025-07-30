#!/usr/bin/env python3
"""
Dynamic Theming System for Autonomous SaaS Factory
Maps business categories to appropriate color schemes and design themes
"""

import re
from typing import Dict, Any, Tuple

class DynamicThemingSystem:
    """Generate topic-appropriate color schemes and themes for SaaS products"""
    
    def __init__(self):
        self.theme_mappings = {
            'medical': {
                'primary_colors': {
                    50: '#f0f9ff',
                    100: '#e0f2fe', 
                    200: '#bae6fd',
                    300: '#7dd3fc',
                    400: '#38bdf8',
                    500: '#0ea5e9',
                    600: '#0284c7',
                    700: '#0369a1',
                    800: '#075985',
                    900: '#0c4a6e'
                },
                'accent_colors': {
                    50: '#f8fafc',
                    100: '#f1f5f9',
                    200: '#e2e8f0',
                    300: '#cbd5e1',
                    400: '#94a3b8',
                    500: '#64748b',
                    600: '#475569',
                    700: '#334155',
                    800: '#1e293b',
                    900: '#0f172a'
                },
                'background': 'from-blue-50 via-white to-blue-50',
                'icon': 'fa-heartbeat',
                'description_theme': 'professional medical solutions'
            },
            
            'finance': {
                'primary_colors': {
                    50: '#f0fdf4',
                    100: '#dcfce7',
                    200: '#bbf7d0',
                    300: '#86efac',
                    400: '#4ade80',
                    500: '#22c55e',
                    600: '#16a34a',
                    700: '#15803d',
                    800: '#166534',
                    900: '#14532d'
                },
                'accent_colors': {
                    50: '#fffbeb',
                    100: '#fef3c7',
                    200: '#fde68a',
                    300: '#fcd34d',
                    400: '#fbbf24',
                    500: '#f59e0b',
                    600: '#d97706',
                    700: '#b45309',
                    800: '#92400e',
                    900: '#78350f'
                },
                'background': 'from-green-50 via-white to-emerald-50',
                'icon': 'fa-chart-line',
                'description_theme': 'financial technology and investment solutions'
            },
            
            'ai': {
                'primary_colors': {
                    50: '#faf5ff',
                    100: '#f3e8ff',
                    200: '#e9d5ff',
                    300: '#d8b4fe',
                    400: '#c084fc',
                    500: '#a855f7',
                    600: '#9333ea',
                    700: '#7c3aed',
                    800: '#6b21a8',
                    900: '#581c87'
                },
                'accent_colors': {
                    50: '#ecfeff',
                    100: '#cffafe',
                    200: '#a5f3fc',
                    300: '#67e8f9',
                    400: '#22d3ee',
                    500: '#06b6d4',
                    600: '#0891b2',
                    700: '#0e7490',
                    800: '#155e75',
                    900: '#164e63'
                },
                'background': 'from-purple-50 via-white to-cyan-50',
                'icon': 'fa-brain',
                'description_theme': 'artificial intelligence and smart automation'
            },
            
            'education': {
                'primary_colors': {
                    50: '#fff7ed',
                    100: '#ffedd5',
                    200: '#fed7aa',
                    300: '#fdba74',
                    400: '#fb923c',
                    500: '#f97316',
                    600: '#ea580c',
                    700: '#c2410c',
                    800: '#9a3412',
                    900: '#7c2d12'
                },
                'accent_colors': {
                    50: '#fefce8',
                    100: '#fef9c3',
                    200: '#fef08a',
                    300: '#fde047',
                    400: '#facc15',
                    500: '#eab308',
                    600: '#ca8a04',
                    700: '#a16207',
                    800: '#854d0e',
                    900: '#713f12'
                },
                'background': 'from-orange-50 via-white to-yellow-50',
                'icon': 'fa-graduation-cap',
                'description_theme': 'educational technology and learning platforms'
            },
            
            'ecommerce': {
                'primary_colors': {
                    50: '#fef2f2',
                    100: '#fee2e2',
                    200: '#fecaca',
                    300: '#fca5a5',
                    400: '#f87171',
                    500: '#ef4444',
                    600: '#dc2626',
                    700: '#b91c1c',
                    800: '#991b1b',
                    900: '#7f1d1d'
                },
                'accent_colors': {
                    50: '#fdf2f8',
                    100: '#fce7f3',
                    200: '#fbcfe8',
                    300: '#f9a8d4',
                    400: '#f472b6',
                    500: '#ec4899',
                    600: '#db2777',
                    700: '#be185d',
                    800: '#9d174d',
                    900: '#831843'
                },
                'background': 'from-red-50 via-white to-pink-50',
                'icon': 'fa-shopping-cart',
                'description_theme': 'e-commerce and retail solutions'
            },
            
            'default': {
                'primary_colors': {
                    50: '#eef2ff',
                    100: '#e0e7ff',
                    200: '#c7d2fe',
                    300: '#a5b4fc',
                    400: '#818cf8',
                    500: '#6366f1',
                    600: '#4f46e5',
                    700: '#4338ca',
                    800: '#3730a3',
                    900: '#312e81'
                },
                'accent_colors': {
                    50: '#f8fafc',
                    100: '#f1f5f9',
                    200: '#e2e8f0',
                    300: '#cbd5e1',
                    400: '#94a3b8',
                    500: '#64748b',
                    600: '#475569',
                    700: '#334155',
                    800: '#1e293b',
                    900: '#0f172a'
                },
                'background': 'from-slate-50 via-white to-indigo-50',
                'icon': 'fa-rocket',
                'description_theme': 'innovative business solutions'
            }
        }
        
        self.category_keywords = {
            'medical': ['health', 'medical', 'healthcare', 'patient', 'doctor', 'clinic', 'hospital', 'wellness', 'fitness', 'therapy'],
            'finance': ['finance', 'fintech', 'payment', 'banking', 'investment', 'trading', 'crypto', 'expense', 'budget', 'invoice', 'billing'],
            'ai': ['ai', 'artificial intelligence', 'machine learning', 'ml', 'smart', 'intelligent', 'automation', 'neural', 'algorithm'],
            'education': ['education', 'learning', 'course', 'student', 'teacher', 'school', 'university', 'training', 'tutorial', 'knowledge'],
            'ecommerce': ['ecommerce', 'e-commerce', 'shop', 'store', 'retail', 'product', 'inventory', 'marketplace', 'sales', 'customer']
        }
    
    def detect_category(self, idea_text: str) -> str:
        """Detect the business category from idea text"""
        idea_lower = idea_text.lower()
        
        category_scores = {}
        for category, keywords in self.category_keywords.items():
            score = sum(1 for keyword in keywords if keyword in idea_lower)
            if score > 0:
                category_scores[category] = score
        
        if category_scores:
            return max(category_scores.items(), key=lambda x: x[1])[0]
        return 'default'
    
    def get_theme_for_idea(self, idea_text: str) -> Dict[str, Any]:
        """Get complete theme configuration for an idea"""
        category = self.detect_category(idea_text)
        theme = self.theme_mappings[category].copy()
        theme['category'] = category
        return theme

if __name__ == "__main__":
    theming = DynamicThemingSystem()
    
    test_ideas = [
        "AI-Powered Content Optimizer – API(s): OpenAI, Analytics – Pricing: $19/month – Moat: machine learning optimization algorithms",
        "Smart Expense Tracker – API(s): Plaid, OpenAI – Pricing: $12/month – Moat: AI-powered categorization and insights",
        "Medical Patient Portal – API(s): Healthcare APIs – Pricing: $25/month – Moat: HIPAA compliant patient management",
        "FinTech Investment Tracker – API(s): Trading APIs – Pricing: $15/month – Moat: real-time portfolio analytics",
        "E-Learning Platform – API(s): Video APIs – Pricing: $20/month – Moat: personalized learning paths"
    ]
    
    for idea in test_ideas:
        theme = theming.get_theme_for_idea(idea)
        print(f"Idea: {idea[:50]}...")
        print(f"Category: {theme['category']}")
        print(f"Primary Color: {theme['primary_colors'][500]}")
        print(f"Icon: {theme['icon']}")
        print("---")
